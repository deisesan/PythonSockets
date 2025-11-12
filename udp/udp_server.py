# UPD Server Side 
import socket

# Criar um socket do lado do servidos 
# Usar IPV4 (AF_INET) e UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o novo socket a uma tupla (endereço IP, endereço da porta)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Não escuta ou aceita conexões 
# UDP é um protocolo sem conexão
message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)