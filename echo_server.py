import socket as st


server_socket = st.socket(st.AF_INET, st.SOCK_STREAM)
server_socket.setsockopt(st.SOL_SOCKET, st.SO_REUSEADDR, 1)

server_address = '127.0.0.1', 8000
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'Получен запрос на подключение от {client_address}.')
    buffer = b''
    while buffer[-2::] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f'Получены данные: {data}.')
            buffer += data
    print(f'Полные данные: {buffer}.')
    connection.sendall(buffer)
finally:
    server_socket.close()
