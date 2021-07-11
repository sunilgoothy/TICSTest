import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')
    
    writer.write("start".encode())
    await writer.drain()
    
    for i in range(1000000):
        # print(i)
        writer.write(str(i).encode())
        await writer.drain()
        # await asyncio.sleep(0.0001)
        
    writer.write("end".encode())
    await writer.drain()  
      
    await asyncio.sleep(1)
    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World from Client!'))