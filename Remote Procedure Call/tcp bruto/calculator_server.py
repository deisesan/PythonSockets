# Server Side RPC Calculator
import socket

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print(f"Servidor iniciado em {HOST_IP}:{HOST_PORT}")
print("Aguardando conexões...")

def calculadora(operacao, num1, num2):
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtracao":
        return num1 - num2
    elif operacao == "multiplicacao":
        return num1 * num2
    elif operacao == "divisao":
        return num1 / num2

client_socket, client_address = server_socket.accept()
print(f"Nova conexão estabelecida com {client_address}")

while True:
    mensagem = client_socket.recv(BYTESIZE).decode(ENCODER)
    
    if not mensagem:
        break
    
    print(f"Mensagem do {client_address}: {mensagem}")
    partes = mensagem.strip().split()
    
    operacao = partes[0].lower()
    num1 = float(partes[1])
    num2 = float(partes[2])
    resultado = calculadora(operacao, num1, num2)

    client_socket.send(str(resultado).encode(ENCODER))
    print(f"Resposta enviada para {client_address}: {resultado}")