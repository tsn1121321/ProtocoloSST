import os
import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6000
BUFFER_SIZE = 4096  
OUTPUT_FOLDER = 'cliente'  

def receive_file(client_socket, filename, file_size):
    bytes_received = 0
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)  

    with open(output_path, 'wb') as f:
        while bytes_received < file_size:
            packet_size_str = client_socket.recv(10).decode()
            packet_size = int(packet_size_str)
            data = client_socket.recv(packet_size)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)
    client_socket.close()

    print(f'Arquivo "{filename}" recebido com sucesso em "{output_path}".')

def receive_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f'Conectado ao servidor {SERVER_HOST}:{SERVER_PORT}')

    file_size_str = client_socket.recv(10).decode()
    file_size = int(file_size_str)
    print(f'Tamanho do arquivo a ser recebido: {file_size} bytes')

    filename = 'teste.zip'

    receive_file(client_socket, filename, file_size)

if __name__ == '__main__':
    receive_data()

