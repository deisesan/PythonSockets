import threading

# Threading para que os programas possam executar multiplas tasks ao mesmo tempo. 
# Cada tarefa roda em uma thread
# Cada thread pode ser rodada simultaneament e compartilha dados umas com as outras.

# Toda thread que inicia pode pfazer algo, então pode ser definido como uma função.
# As thread vão direcionar essas funções
# Quando iniciar as threas, as funções podem ser executadas 

def function1():
    for x in range(10):
        print("ONE ")

def function2():
    for x in range(10):
        print("TWO ")

def function3():
    for x in range(10):
        print("THREE ")

# Se chamar as funcções, vai mostrar a primeira função que teve a chamada completada antes da próxima
# São executadas linearmente
# function1()
# function2()
# function3()

# Executar as funções concorretemente usando threads. 
# Usar a target para uma thread
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

# t1.start()
# t2.start()
# t3.start()

# Threads só podem ser executados uma vez. Se quiser reusar, você pode redefinir. 
t1 = threading.Thread(target=function1)
t1.start()

# É possível pausar o programa principal até uma thread está pronta
t1 = threading.Thread(target=function1)
t1.start()
t1.join() # Pausa o prorgrama principal até essa thread estar completa
print("Regras da Threarding!")