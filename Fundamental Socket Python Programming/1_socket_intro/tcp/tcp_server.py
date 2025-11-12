#TCP Server Side 

# Importar o módulo do socket 
import socket

# Criar um socket do lado do servidor
# Usando IPV4 (AF_INET) e TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Como pegar o Endereço IP dinamicamente 
# print(socket.gethostname()) #hostname
# print(socket.gethostbyname(socket.gethostname())) #IP do hostname

# Vincular o novo socket a uma tupla (endereço IP, endereço da porta)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Colocar o socket no modo de escuta para ouvir quaisquer conexões possíveis
server_socket.listen()

# Ouvindo para sempre para aceitar qualquer (ANY) conexão
while True:
    # Aceita todas as conexões únicas e armazena dois pedaços da informação
    client_socket, client_address = server_socket.accept()
    # print(type(client_socket))
    # print(client_socket)
    # print(type(client_address))
    # print(client_address)

    print(f"Conectado a {client_address}!\n")

    # Enviando uma mensagem para o cliente que se conectou
    client_socket.send("Você está conectado!".encode("utf-8"))

    # Fechar o socket do servidor 
    server_socket.close()
    break