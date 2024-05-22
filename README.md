# ProtocoloSST
Vamos ao passo a passo de como implementar o código e fazer os testes:

1° Passo - Faça o download do Visual Studio Code ou da IDE de sua preferência que seja compatível com Python. É através dela que executaremos o código e testes de simulação do uso do protocolo SST. Você pode fazer o download do Visual Studio Code através do link: <https://code.visualstudio.com/download>.

2° Passo - Verifique se o Python está instalado corretamente na máquina em que vai ser realizado os testes através do código ‘python –version’ dentro do prompt de comando.
Caso o Python não esteja instalado na sua máquina, você pode fazer o download através do link: <https://www.python.org/downloads/>.

3° Passo - Crie uma pasta chamada ‘envio de arquivos’ na pasta documentos, após isso, dentro dessa pasta envio de arquivos, crie mais duas pastas, uma chamada ‘servidor’ e outra chamada ‘cliente’. 
	Dentro da pasta ‘servidor’ ficará os códigos e o arquivo que você deseja enviar para a pasta ‘cliente’, para demonstração do uso do protocolo, deixe um arquivo de tamanho grande dentro da pasta servidor, o arquivo deve estar nomeado como ‘teste’ e compactado no formato zip. Vamos deixar um arquivo de exemplo caso queira fazer o download para testes: <https://drive.google.com/drive/folders/16aIHVTDtX1tVTM1qs8vm3kRoyG9muPnN?usp=drive_link>.
	Após as pastas criadas, abra as mesmas dentro da sua IDE. 

4° Passo - Navegue até a pasta ‘servidor’ dentro da IDE, clique com o botão direito do mouse e selecione a opção ‘new file’, nomeie o arquivo como ‘server.py’, dentro do arquivo cole o seguinte código:

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



5° Passo - Refaça o processo anterior, porém dessa vez renomeie o arquivo para “client.py” e cole o seguinte código:


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

6° Passo -  Pronto, agora nosso ambiente de trabalho está pronto para executar a simulação do protocolo SST. Com o arquivo compactado nomeado corretamente e os códigos executando, dentro do visual Studio vá até a aba terminal e clique em ‘split terminal’.


7° Passo - Em um dos terminais execute o código ‘python server.py’ e em outro execute o código ‘python client.py’. 


8° Passo - Após a execução desses códigos, você receberá a mensagem de sucesso e o arquivo será transferido para a pasta de destino, no nosso caso, para a pasta ‘cliente’.


Segue link de formulário para feedback: <>
