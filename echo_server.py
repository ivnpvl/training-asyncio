import asyncio
import socket as st
from asyncio import AbstractEventLoop as AELoop


async def echo(connection: st.socket, loop: AELoop) -> None:
    while data := await loop.sock_recv(connection, 1024):
        await loop.sock_sendall(connection, data)


async def listen_for_connection(server_socket: st.socket, loop: AELoop):
    while True:
        connection, client_address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {client_address}.')
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = st.socket(st.AF_INET, st.SOCK_STREAM)
    server_socket.setsockopt(st.SOL_SOCKET, st.SO_REUSEADDR, 1)
    server_address = '127.0.0.1', 8000
    server_socket.bind(server_address)
    server_socket.setblocking(False)
    server_socket.listen()
    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
