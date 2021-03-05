import socket, redis
import sys, signal, threading, time


class TCPServer:
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(3)

        # Bind the socket to the port
        self.server_address = ('192.168.10.140', 25001)
        print( 'starting up on %s port %s' % self.server_address)
        self.sock.bind(self.server_address)
        self._tryStop = False
        self._stopped = False
        self.waiting = True
        self.message_ctr = 0
        self.output = list()

        # Redis client
        self.rclient = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses = True)

    def listen(self):
        # Listen for incoming connections
        self.sock.listen(1)
        lst_data = list()
        while not self._tryStop:
            # Wait for a connection
            print( 'waiting for a connection')
            self.waiting = True
            try:
                self.connection, self.client_address = self.sock.accept()
                self.message_ctr += 1
                self.waiting = False
                try:
                    print( 'connection from', self.client_address)
                    ctr = 0
                    while not self._tryStop:
                        msg = str(self.rclient.hgetall('tagread'))
                        msg_body = '5231'
                        msg_len = len(msg_body)
                        #msg = f'00{msg_len}P_SENDTCPMSG{ctr}{msg_body}' + "\x03"
                        msg = f'{ctr}' + "\x03"
                        msg_byte = msg.encode('utf-8')
                        print(f'{msg} {msg_byte}')
                        self.connection.sendall(msg_byte)
                        ctr += 1
                        # if ctr >= 10:
                        #     ctr = 0
                        time.sleep(1)
                    # Receive the data in small chunks
                    while True:
                        data = self.connection.recv(16)
                        print( 'received "%s"' % data)
                        if data:
                            print( 'sending data back to the client')
                            lst_data.append(data)
                            #self.connection.sendall(data)
                        else:
                            print( 'no more data from', self.client_address)
                            self.output = lst_data
                            break
                except socket.timeout:
                    print( "Closing connection due to time out")
                    self.connection.close()
                except ConnectionResetError:
                    print(f'Connection reset occurred in host machine')
                except ConnectionAbortedError:
                    print(f'Connection aborted in host machine')
                except OSError:
                    if self._tryStop:
                        print(f'Shutdown in progress, aborting receive')
                finally:
                    print(self.output)
                    # Clean up the connection
                    print( "Closing connection")
                    self.connection.close()
            except socket.timeout:
                print('Socket timeout')

        self._stopped = True
        print( "Server Stopped")

    def stop(self):
        self._tryStop = True
        self.connection.close()

if __name__ == '__main__':
    server = TCPServer()
    t = threading.Thread(target=server.listen)
    t.daemon = True
    t.start()
    _count = 0
    _msgCtr = server.message_ctr
    while True:
        if server._stopped:
            break
        if server.waiting:
            _count +=1
        if _msgCtr != server.message_ctr:
            print('watchdog timer reset, message sent: ', server.message_ctr)
            _count = 0
        try:
            if _count > 600:
                print('Shutdown server: timeout ')
                server.stop = True
                break
            _msgCtr = server.message_ctr
            time.sleep(1)

        except KeyboardInterrupt:
            print('Shutdown server')
            server.stop()
            time.sleep(3)
            sys.exit(0)