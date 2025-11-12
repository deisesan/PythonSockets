# Chat Client Side 
import socket

# Define as constants 
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Cria um socket client e conecta no servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# Enviar e receber mensagens
while True:
    # Receba informação do servidor
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # Sair se o servidor quiser sair, senão continuar enviando as mensagens
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nAcabou o chat...Tchau!")
        break
    else:
        print(f"\n{message}")
        message = input("Message: ")
        client_socket.send(message.encode(ENCODER))

# Fechar o client socket
client_socket.close()