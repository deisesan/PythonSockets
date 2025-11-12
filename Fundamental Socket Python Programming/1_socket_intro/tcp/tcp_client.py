# TCP Client Side 

# Importar o módulo do socket 
import socket

# Criar um socket do lado do cliente
# Usando IPV4 (AF_INET) e TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket a um servidor local com um endereço IP e uma porta
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# Recebe a mensagem do servidor 
# Especificar o máximo de número dos bytes para receber 
message = client_socket.recv(1024)
print(message.decode("utf-8"))
# print(type(message))

# Fechar o socket do cliente 
client_socket.close()