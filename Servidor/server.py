import socket
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6000
BUFFER_SIZE = 4096 

def send_file(client_socket, filename):
    with open(filename, 'rb') as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            packet = f'{len(bytes_read):<10}'.encode() + bytes_read
            client_socket.sendall(packet)
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f'Servidor iniciado em {SERVER_HOST}:{SERVER_PORT}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Conexão recebida de {client_address}')

        filename = 'teste.zip'

        file_size = os.path.getsize(filename)
        client_socket.send(f'{file_size:<10}'.encode())

        send_file(client_socket, filename)

if __name__ == '__main__':
    start_server()
