# Client Side RPC Calculator usando XML-RPC
import xmlrpc.client
import socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345

server_url = f"http://{DEST_IP}:{DEST_PORT}"
print(f"Conectando ao servidor RPC em {server_url}...")

try:
    proxy = xmlrpc.client.ServerProxy(server_url, allow_none=True)
    print("Conectado ao servidor!\n")
    
    while True:
        comando = input("Cliente: ").strip()
        
        if comando.lower() == "sair":
            print("\nEncerrando conexão...")
            break
        
        if not comando:
            continue
        
        try:
            partes = comando.strip().split()
            
            if len(partes) != 3:
                print("ERRO: Formato inválido. Use: operacao num1 num2\n")
                continue
            
            operacao = partes[0].lower()
            num1 = float(partes[1])
            num2 = float(partes[2])
            
            if operacao == "soma":
                resultado = proxy.soma(num1, num2)
            elif operacao == "subtracao":
                resultado = proxy.subtracao(num1, num2)
            elif operacao == "multiplicacao":
                resultado = proxy.multiplicacao(num1, num2)
            elif operacao == "divisao":
                resultado = proxy.divisao(num1, num2)
            else:
                print(f"ERRO: Operação '{operacao}' não reconhecida.\n")
                print("Operações disponíveis: soma, subtracao, multiplicacao, divisao\n")
                continue
            
            print(f"Servidor: {resultado}\n")
            
        except ValueError as e:
            print(f"ERRO: {str(e)}\n")
        except xmlrpc.client.Fault as e:
            print(f"ERRO no servidor: {e.faultString}\n")
        except Exception as e:
            print(f"ERRO: {str(e)}\n")
            
except ConnectionRefusedError:
    print("ERRO: Não foi possível conectar ao servidor. Certifique-se de que o servidor está rodando.")
except Exception as e:
    print(f"ERRO de conexão: {str(e)}")

print("Conexão encerrada.")

