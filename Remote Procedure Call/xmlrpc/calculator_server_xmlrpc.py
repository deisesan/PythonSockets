# Server Side RPC Calculator usando XML-RPC
from xmlrpc.server import SimpleXMLRPCServer
import socket

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

server = SimpleXMLRPCServer((HOST_IP, HOST_PORT), allow_none=True)
print(f"Servidor RPC iniciado em {HOST_IP}:{HOST_PORT}")
print("Aguardando chamadas remotas...")

class CalculadoraRPC:
    def soma(self, num1, num2):
        resultado = num1 + num2
        print(f"Chamada remota: soma({num1}, {num2}) = {resultado}")
        return resultado
    
    def subtracao(self, num1, num2):
        resultado = num1 - num2
        print(f"Chamada remota: subtracao({num1}, {num2}) = {resultado}")
        return resultado
    
    def multiplicacao(self, num1, num2):
        resultado = num1 * num2
        print(f"Chamada remota: multiplicacao({num1}, {num2}) = {resultado}")
        return resultado
    
    def divisao(self, num1, num2):
        if num2 == 0:
            raise ValueError("Divisão por zero não permitida")
        resultado = num1 / num2
        print(f"Chamada remota: divisao({num1}, {num2}) = {resultado}")
        return resultado

calculadora = CalculadoraRPC()
server.register_instance(calculadora)

server.register_function(calculadora.soma, 'soma')
server.register_function(calculadora.subtracao, 'subtracao')
server.register_function(calculadora.multiplicacao, 'multiplicacao')
server.register_function(calculadora.divisao, 'divisao')

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServidor encerrado.")

