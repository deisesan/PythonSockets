# Client Side RPC Calculator
import socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345 
ENCODER = "utf-8"
BYTESIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))
print("Conectado ao servidor!\n")

while True:
    comando = input("Cliente: ").strip()
    
    if comando.lower() == "sair":
        print("\nEncerrando conexão...")
        break
    
    if not comando:
        continue
    
    partes = comando.strip().split()   
    operacao = partes[0].lower()
    num1 = float(partes[1])
    num2 = float(partes[2])
        
    requisicao = f"{operacao} {num1} {num2}"
    client_socket.send(requisicao.encode(ENCODER))
    resultado = client_socket.recv(BYTESIZE).decode(ENCODER)
    print(f"Servidor: {resultado}\n")

client_socket.close()
print("Conexão encerrada.")
