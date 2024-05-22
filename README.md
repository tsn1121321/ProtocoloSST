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

1. Navegue até a pasta `servidor` e crie o arquivo `server.py` com o determinado conteúdo presente no repositório correspondendete ao servidor;


2. Coloque um arquivo grande chamado `teste.zip` na pasta `servidor`.


3. Abra um terminal no Visual Studio Code e navegue até a pasta `servidor`:

    cd caminho/para/envio_de_arquivos/servidor

4. Execute o servidor:
   
   python server.py
   

# Configuração e Execução do Cliente

1. Navegue até a pasta `cliente` e crie o arquivo `client.py` com o com o determinado conteúdo presente no repositório correspondendete ao cliente;


2. Abra um novo terminal no Visual Studio Code e navegue até a pasta `cliente`:
   
   cd caminho/para/envio_de_arquivos/cliente
   

3. Execute o cliente:
   
   python client.py


# Verificação da Transferência

Após a execução dos códigos, verifique se o arquivo `teste.zip` foi transferido corretamente para a pasta `cliente`. A mensagem de sucesso no terminal do cliente deve confirmar a transferência.

# Conclusão

Este projeto demonstra a implementação básica de um protocolo de transferência de arquivos utilizando sockets em Python. Ele pode ser expandido e melhorado com funcionalidades adicionais, como suporte a múltiplos clientes, criptografia dos dados transferidos, e verificação de integridade dos arquivos.


# Links
Link do drive para download de arquivo de exemplo: <https://drive.google.com/drive/folders/16aIHVTDtX1tVTM1qs8vm3kRoyG9muPnN?usp=drive_link>

Link de formulário para feedback: <https://docs.google.com/forms/d/e/1FAIpQLSfE-b9wr9iS5bOMMWIzGhZ13SuQ_yW93AGtBIcOG6rU-qEXRg/viewform?vc=0&c=0&w=1&flr=0>
