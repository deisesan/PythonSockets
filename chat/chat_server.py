# Chat Server Side 
import socket

# Defina constants
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Criar um socket servidor (TCP e IPV4), vincular ip/port e escutar
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Aceitar qualquer conexão e mostrar
print("Servidor está rodando...")
client_socket, client_addresss = server_socket.accept()
client_socket.send("Você está conectado no servidor...\n".encode(ENCODER))