# Install TICSUtil using below command:
#   pip install --upgrade git+https://github.com/TMIND-PA/TICSUtil.git

import asyncio, redis, json, sys, signal, csv, os, platform, socket
from datetime import datetime
from TICSUtil import readconfigfile,TICSLogger

# config file
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(os.path.abspath(sys.executable))
elif __file__:
    application_path = os.path.dirname(os.path.abspath(__file__))

APPLICATION_PATH =  application_path 
COMPUTER_NAME = platform.node()  
config_file = os.path.join(APPLICATION_PATH, 'TCPConfig.ini')

try:
    os.environ['LOG_FILENAME'] = readconfigfile(config_file, 'logger_config', 'file')
    os.environ['LOG_FILE_DIR'] = readconfigfile(config_file, 'logger_config', 'location')
    os.environ['LOG_MAXSIZE'] = readconfigfile(config_file, 'logger_config', 'max_size')
    os.environ['LOG_BACKUP_COUNT'] = readconfigfile(config_file, 'logger_config', 'backup_count')
    os.environ['LOGGER_NAME'] = 'TICSTCPLog'
    console_level = readconfigfile(config_file, 'logger_config', 'console_level')
    file_level = readconfigfile(config_file, 'logger_config', 'file_level')

except:
    os.environ['LOG_FILENAME'] = 'TCPGateway.log'
    os.environ['LOG_FILE_DIR'] = r'C:\TICS\TICSTCPGateway\logs'

os.environ['LOGGER_NAME'] = 'TICSTCPLog'

#Initialize logger 
Logger = TICSLogger()
Logger.console_dbglevel(console_level)
Logger.file_dbglevel(file_level)
Log = Logger.get_log

class TicsTCPAsyncGW:

    def __init__(self, tagFileName='tags.csv', heartBeatTag='tcp_heartbeat'):
        self.is_client_connected = False
        self.is_server_connected = False
        self.prevHB = 0
        self.unchanged = 0
        self.first_connect_pending = True
        self.heartBeatTag = heartBeatTag
        self.tagFilename = tagFileName
        self.stop = False

    async def read_tag_file(self, filename):
        """Read tags from a csv file and store them in redis hash called tagdb."""
        # print(log_time(), f'<INFO>read_tag_file')
        Log.info(f'Initiating read_tag_file....')
        try:
            root = os.path.dirname(os.path.realpath(__file__))
            filename = os.path.join(root,filename)
            with open(filename) as tags_file:
                csv_reader = csv.DictReader(tags_file, delimiter=',')
                line_count = 0
                # rclient.delete('tcptagdb')
                for row in csv_reader:
                    commented_line = row['tag_name'].startswith('#')
                    if ( not commented_line ):
                        # Log.debug(f"line {row}, line type {type(row)}")
                        msgname = row['msg_name']
                        tagname = row['tag_name']
                        # TODO: Implement pipelining to insert multiple values.
                        # Refer realpython article on redis https://realpython.com/python-redis/#example-pyhatscom
                        rclient.hset('tcp:'+msgname, tagname, json.dumps(row))
                    line_count+=1
                Log.info(f'Processed {line_count} lines from {filename}.')     
        except ConnectionRefusedError as CnErr:
            self.is_connected = False
            Log.error(f"startserver: {str(CnErr)}")
        except Exception as e:
            self.is_connected = False
            Log.error(f"CSV Read Error: {filename}, Error:{e}")
            
        Log.info("Exiting read_tag_file....")   
        

    async def handle_msg(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()

        print("Close the connection")
        writer.close()
        
    async def startserver(self, host, port):
        Log.info(f'Connecting to server at {host} on port {port}')
        self.server = await asyncio.start_server(self.handle_msg, host, port)
        self.is_server_connected = True  
        addr = self.server.sockets[0].getsockname()
        print(f'Serving on {addr}')
        async with self.server:
            await self.server.serve_forever()

    async def startclient(self, host, port):
        while (not self.stop):
            try:
                if (not self.is_client_connected):
                    self.reader, self.writer = await asyncio.open_connection(host, port)
                    self.is_client_connected = True
                    Log.info(f"TCP Client connected to {host} on port {port}")
            except Exception as e:
                self.is_client_connected = False
                Log.error(f"Unable to connect to TCP server. Error {e}")
            
            await asyncio.sleep(3)

    async def send_msg(self, msg):
        try:
            self.writer.write(msg.encode())
            await self.writer.drain()
            Log.debug(f'Sending Message: {msg!r}')
        except Exception as e:
            self.is_client_connected = False
            Log.error(f"Error in client while sending message. Error {e}")

    async def recv_msg(self):
        Log.debug(f'Starting Client Receive message loop.....')
        while (not self.stop):
            try:
                if (self.is_client_connected):
                    data = await self.reader.read(1024)
                    msg = data.decode()
                    Log.debug(f'Received Message: {msg!r}')
                    if (msg == ''):
                        if (not self.stop):
                            Log.warning(f'Received NULL Message. Setting connection status to close.')
                        self.is_client_connected = False                    
            except Exception as e:
                self.is_client_connected = False
                Log.error(f"Error in client receiving msg . Error {e}")

            await asyncio.sleep(0.001)

        # self.writer.close()
        await self.writer.wait_closed()
        Log.debug(f'Client Connection closed.')


    async def debugconsole(self):
        await asyncio.sleep(5)
        while (not self.stop):
            await self.send_msg('Hello World from Client!')
            await asyncio.sleep(5)

    async def debugNone(self):
        pass

def checkRedis():
    Log.info("Connecting to shared memory server...")
    try:
        rclient.ping()
        return True
    except Exception as e:
        Log.error(f"Error in connecting to shared memory: {e}") 
        return False

# main function of the module
async def main():
    global rclient
    global exitprocess
    
    exitprocess = False
    def exit_request(sig, frame):
        global exitprocess
        Log.info(f'Stop Request received from User')

        Log.warning(f'Shutting down TCP Server.....')
        TCPServer.server.close()

        Log.warning(f'Closing Client Connection.....')
        TCPServer.writer.close()

        TCPServer.stop = True
        exitprocess = True

    signal.signal(signal.SIGINT, exit_request)

    debug = 0
    global config_file
    i = 0
    for arg in sys.argv:
        if (arg.lower() == 'debug'):
            debug = 1
        if (arg.lower() == '-debug'):
            debug = 1
        if (arg.lower() == '-c'):
            config_file = sys.argv[i+1]
        i+=1

    Log.info(f"Application Path: {APPLICATION_PATH}")
    Log.info(f"Reading Config File: {config_file}")
    client_host = readconfigfile(config_file, 'TCP_Client', 'host')
    client_port = readconfigfile(config_file, 'TCP_Client', 'port')
    server_host = readconfigfile(config_file, 'TCP_Server', 'host')
    server_port = readconfigfile(config_file, 'TCP_Server', 'port')
    heartbeat_tag = readconfigfile(config_file, 'TCP_Server', 'heartbeat_tag')
    tag_file = readconfigfile(config_file, 'TCP_Server', 'tag_file')
    prj_code = readconfigfile(config_file, 'PRJ_Config', 'prj_code')
    Log.info(f'Project Code: {prj_code}')

    #Redis Connection.
    redis_host = readconfigfile(config_file, 'shared_mem', 'host')
    redis_port = readconfigfile(config_file, 'shared_mem', 'port')
    rclient = redis.Redis(host=redis_host, port=redis_port, db=prj_code, decode_responses = True)

    while True:
        if (exitprocess):
            sys.exit(0)
            
        Log.info(f"Starting Client loop...")
        TCPServer = TicsTCPAsyncGW(tagFileName=tag_file, heartBeatTag=heartbeat_tag)
        if (checkRedis()):
            taskServer = loop.create_task(TCPServer.startserver(server_host, server_port))
            taskClient = loop.create_task(TCPServer.startclient(client_host, client_port))
            taskClientRcvMsg = loop.create_task(TCPServer.recv_msg())
            # taskWrite = asyncio.create_task(OPCServer.write_tags())
            # taskWrite = loop.create_task(OPCServer.write_tags())
            # taskHB = loop.create_task(TCPServer.heartbeat())
            if (debug):
                # taskDebug = asyncio.create_task(debugconsole(sub_period))
                taskDebug = loop.create_task(TCPServer.debugconsole())
            else:
                taskDebug = loop.create_task(TCPServer.debugNone())
     
            # await asyncio.wait([taskRead, taskHB, taskWrite, taskDebug])
            await asyncio.wait([taskServer, taskClient, taskClientRcvMsg, taskDebug])
            
        await asyncio.sleep(3)

#Module entry function
if __name__ == '__main__':
    Log.info(f"Starting TCP Gateway....")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    Log.warning("TCP Gateway Stopped")