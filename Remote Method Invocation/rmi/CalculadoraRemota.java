package rmi;

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Interface remota para operações de calculadora
 * Todas as interfaces RMI devem estender Remote
 * Todos os métodos devem declarar RemoteException
 */
public interface CalculadoraRemota extends Remote {

    /**
     * Soma dois números
     * @param a primeiro número
     * @param b segundo número
     * @return resultado da soma
     * @throws RemoteException em caso de erro de rede
     */
    double somar(double a, double b) throws RemoteException;

    /**
     * Subtrai dois números
     * @param a primeiro número
     * @param b segundo número
     * @return resultado da subtração (a - b)
     * @throws RemoteException em caso de erro de rede
     */
    double subtrair(double a, double b) throws RemoteException;

    /**
     * Multiplica dois números
     * @param a primeiro número
     * @param b segundo número
     * @return resultado da multiplicação
     * @throws RemoteException em caso de erro de rede
     */
    double multiplicar(double a, double b) throws RemoteException;

    /**
     * Divide dois números
     * @param a dividendo
     * @param b divisor
     * @return resultado da divisão
     * @throws RemoteException em caso de erro de rede
     * @throws ArithmeticException se o divisor for zero
     */
    double dividir(double a, double b) throws RemoteException, ArithmeticException;
}
