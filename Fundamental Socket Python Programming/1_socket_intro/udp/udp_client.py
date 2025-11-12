# UDP Client Side 
import socket

# Cria um UDP IPV4 Socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia alguma informação via protocolo sem conexão 
client_socket.sendto("olá mundo".encode("utf-8"), (socket.gethostbyname(socket.gethostname()), 12345))