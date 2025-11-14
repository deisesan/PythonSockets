package rmi;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

/**
 * Implementação da calculadora remota
 * Estende UnicastRemoteObject para funcionar como objeto RMI
 */
public class CalculadoraImpl extends UnicastRemoteObject implements CalculadoraRemota {

    /**
     * Construtor - deve declarar RemoteException
     * @throws RemoteException em caso de erro na criação do objeto remoto
     */
    public CalculadoraImpl() throws RemoteException {
        super();
    }

    @Override
    public double somar(double a, double b) throws RemoteException {
        System.out.printf("Executando soma: %.2f + %.2f%n", a, b);
        return a + b;
    }

    @Override
    public double subtrair(double a, double b) throws RemoteException {
        System.out.printf("Executando subtração: %.2f - %.2f%n", a, b);
        return a - b;
    }

    @Override
    public double multiplicar(double a, double b) throws RemoteException {
        System.out.printf("Executando multiplicação: %.2f * %.2f%n", a, b);
        return a * b;
    }

    @Override
    public double dividir(double a, double b) throws RemoteException, ArithmeticException {
        System.out.printf("Executando divisão: %.2f / %.2f%n", a, b);
        if (b == 0) {
            throw new ArithmeticException("Divisão por zero não é permitida!");
        }
        return a / b;
    }

    /**
     * Método principal do servidor
     * Cria e registra o objeto remoto no registry RMI
     */
    public static void main(String[] args) {
        try {
            // Cria uma instância da calculadora
            CalculadoraImpl calculadora = new CalculadoraImpl();

            // Cria o registry RMI na porta 1099 (porta padrão)
            Registry registry = LocateRegistry.createRegistry(1099);

            // Registra o objeto remoto com o nome "Calculadora"
            registry.bind("Calculadora", calculadora);

            System.out.println("Servidor da Calculadora iniciado com sucesso!");
            System.out.println("Registry RMI criado na porta 1099");
            System.out.println("Aguardando conexões de clientes...");

            // Mantém o servidor em execução
            System.out.println("Pressione Ctrl+C para encerrar o servidor");

        } catch (Exception e) {
            System.err.println("Erro no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
