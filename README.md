# Simulação de Protocolo SST para Transferência de Arquivos

Este projeto demonstra uma simulação do protocolo SST (Simulação de Transferência Segura) para transferência de arquivos entre um servidor e um cliente utilizando sockets em Python.

# Requisitos

- Python 3.x
- IDE ou editor de texto compatível com Python (recomendado: Visual Studio Code)

# Configuração do Ambiente

1. **Instale o Python**:
   Verifique se o Python está instalado:
   ```sh
   python --version
   ```
   Caso não esteja, faça o download e instale o Python através do [site oficial](https://www.python.org/downloads/).

2. **Instale o Visual Studio Code**:
   Faça o download do Visual Studio Code através do [site oficial](https://code.visualstudio.com/download).

3. **Clone o Repositório ou Baixe os Arquivos**:
   Estruture os arquivos conforme mostrado na seção "Estrutura do Projeto".

# Configuração e Execução do Servidor

1. Navegue até a pasta `servidor` e crie o arquivo `server.py` com o seguinte conteúdo:

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
  

2. Coloque um arquivo grande chamado `teste.zip` na pasta `servidor`.

3. Abra um terminal no Visual Studio Code e navegue até a pasta `servidor`:

    cd caminho/para/envio_de_arquivos/servidor

4. Execute o servidor:
   
   python server.py
   

## Configuração e Execução do Cliente

1. Navegue até a pasta `cliente` e crie o arquivo `client.py` com o seguinte conteúdo:

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
   

2. Abra um novo terminal no Visual Studio Code e navegue até a pasta `cliente`:
   
   cd caminho/para/envio_de_arquivos/cliente
   

3. Execute o cliente:
   
   python client.py


# Verificação da Transferência

Após a execução dos códigos, verifique se o arquivo `teste.zip` foi transferido corretamente para a pasta `cliente`. A mensagem de sucesso no terminal do cliente deve confirmar a transferência.

# Conclusão

Este projeto demonstra a implementação básica de um protocolo de transferência de arquivos utilizando sockets em Python. Ele pode ser expandido e melhorado com funcionalidades adicionais, como suporte a múltiplos clientes, criptografia dos dados transferidos, e verificação de integridade dos arquivos.


# Segue link de formulário para feedback: <>
# Segue link do drive para download de arquivo de exemplo: <https://drive.google.com/drive/folders/16aIHVTDtX1tVTM1qs8vm3kRoyG9muPnN?usp=drive_link>
