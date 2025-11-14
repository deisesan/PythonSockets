# Calculadora Remota - Java RMI

Esta é uma aplicação de calculadora remota implementada usando Java RMI (Remote Method Invocation).

## Estrutura do Projeto

- **CalculadoraRemota.java** - Interface remota que define os métodos disponíveis
- **CalculadoraImpl.java** - Servidor que implementa a interface e registra o objeto remoto
- **CalculadoraCliente.java** - Cliente que se conecta ao servidor e chama os métodos remotos

## Funcionalidades

A calculadora remota oferece as seguintes operações:
- Soma
- Subtração  
- Multiplicação
- Divisão (com tratamento de divisão por zero)

## Como Executar

### 1. Compilar os arquivos

Abra o terminal na pasta raiz do projeto e execute:

```cmd
javac *.java
```

### 2. Executar o Servidor

Em um terminal, execute:

```cmd
java CalculadoraImpl
```

O servidor será iniciado na porta 1099 (porta padrão do RMI Registry).

### 3. Executar o Cliente

Em outro terminal (deixe o servidor rodando), execute:

```cmd
java CalculadoraCliente
```

### 4. Usar a Calculadora

O cliente apresentará um menu interativo onde você pode:
1. Escolher a operação desejada (1-4)
2. Inserir os dois números
3. Ver o resultado calculado remotamente
4. Repetir ou sair (opção 5)

## Conceitos RMI Demonstrados

### Interface Remota
- Estende `Remote`
- Todos os métodos declaram `RemoteException`
- Define o contrato entre cliente e servidor

### Servidor
- Implementa a interface remota
- Estende `UnicastRemoteObject`
- Cria e registra o objeto no RMI Registry
- Executa as operações e retorna resultados

### Cliente
- Conecta ao RMI Registry
- Obtém referência do objeto remoto via `lookup()`
- Chama métodos como se fossem locais
- Trata exceções de rede

## Tratamento de Exceções

A aplicação trata:
- **RemoteException** - Erros de rede/comunicação RMI
- **ArithmeticException** - Divisão por zero
- **Exception** - Outros erros gerais

## Exemplo de Uso

```
=== CALCULADORA REMOTA ===
Conectado ao servidor com sucesso!

Escolha uma operação:
1. Somar
2. Subtrair  
3. Multiplicar
4. Dividir
5. Sair
Opção: 1
Digite o primeiro número: 10.5
Digite o segundo número: 5.2
Resultado: 10,50 + 5,20 = 15,70
```

## Observações

- O servidor deve estar rodando antes de executar o cliente
- Por padrão, a aplicação usa localhost na porta 1099
- O cliente pode ser executado múltiplas vezes simultaneamente
