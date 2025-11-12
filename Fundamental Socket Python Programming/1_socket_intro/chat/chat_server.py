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

# Enviar e receber mensagens 
while True:
    # Recebe as informação do client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # Sair se o client socket quiser sair, se não mostrar a mensagem 
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nAcabou o chat...Tchau!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))


# Fechar o server socket
server_socket.close()