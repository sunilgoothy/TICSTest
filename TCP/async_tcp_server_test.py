# https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-server-using-streams

import asyncio
from time import perf_counter

async def handle_echo(reader, writer):
    time_start = 0
    time_end = 0
    try:
        while True:
            data = await reader.read(100)
            message = data.decode()
            # addr = writer.get_extra_info('peername')

            # print(f"Received {message!r} from {addr!r}")
            # print(f"Received {message!r}")
                  
            if 'start' in message:
                time_start = perf_counter()
                
            if 'end' in message:
                time_end = perf_counter()  
                total_time =   time_end - time_start
                print(f"Time Elapsed: {total_time} seconds")
                
            if message == '':
                print("Close the connection")
                writer.close()

            # print(f"Send: {message!r}")
            writer.write(data)
            await writer.drain()
    except Exception as e:
        print(f"Close the connection: {e}")
        writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())