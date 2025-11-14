package rmi;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

/**
 * Cliente da calculadora remota
 * Conecta ao servidor RMI e chama métodos remotos
 */
public class CalculadoraCliente {

    public static void main(String[] args) {
        Scanner scanner = null;
        try {
            // Conecta ao registry RMI no localhost na porta 1099
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);

            // Obtém referência para o objeto remoto "Calculadora"
            CalculadoraRemota calculadora = (CalculadoraRemota) registry.lookup("Calculadora");

            scanner = new Scanner(System.in);

            System.out.println("=== CALCULADORA REMOTA ===");
            System.out.println("Conectado ao servidor com sucesso!");

            while (true) {
                try {
                    System.out.println("\nEscolha uma operação:");
                    System.out.println("1. Somar");
                    System.out.println("2. Subtrair");
                    System.out.println("3. Multiplicar");
                    System.out.println("4. Dividir");
                    System.out.println("5. Sair");
                    System.out.print("Opção: ");

                    if (!scanner.hasNextInt()) {
                        System.out.println("Por favor, digite um número válido!");
                        scanner.nextLine(); // Limpa o buffer
                        continue;
                    }

                    int opcao = scanner.nextInt();

                    if (opcao == 5) {
                        System.out.println("Encerrando cliente...");
                        break;
                    }

                    if (opcao < 1 || opcao > 4) {
                        System.out.println("Opção inválida!");
                        continue;
                    }

                    System.out.print("Digite o primeiro número: ");
                    if (!scanner.hasNextDouble()) {
                        System.out.println("Por favor, digite um número válido!");
                        scanner.nextLine(); // Limpa o buffer
                        continue;
                    }
                    double a = scanner.nextDouble();

                    System.out.print("Digite o segundo número: ");
                    if (!scanner.hasNextDouble()) {
                        System.out.println("Por favor, digite um número válido!");
                        scanner.nextLine(); // Limpa o buffer
                        continue;
                    }
                    double b = scanner.nextDouble();

                    double resultado = 0;
                    String operacao = "";

                    switch (opcao) {
                        case 1:
                            resultado = calculadora.somar(a, b);
                            operacao = String.format("%.2f + %.2f", a, b);
                            break;
                        case 2:
                            resultado = calculadora.subtrair(a, b);
                            operacao = String.format("%.2f - %.2f", a, b);
                            break;
                        case 3:
                            resultado = calculadora.multiplicar(a, b);
                            operacao = String.format("%.2f * %.2f", a, b);
                            break;
                        case 4:
                            resultado = calculadora.dividir(a, b);
                            operacao = String.format("%.2f / %.2f", a, b);
                            break;
                    }

                    System.out.printf("Resultado: %s = %.2f%n", operacao, resultado);

                } catch (ArithmeticException e) {
                    System.err.println("Erro matemático: " + e.getMessage());
                } catch (java.util.InputMismatchException e) {
                    System.err.println("Entrada inválida! Por favor, digite apenas números.");
                    scanner.nextLine(); // Limpa o buffer
                } catch (Exception e) {
                    System.err.println("Erro na operação: " + e.getMessage());
                }
            }

        } catch (Exception e) {
            System.err.println("Erro no cliente: " + e.getMessage());
            e.printStackTrace();
        } finally {
            if (scanner != null) {
                scanner.close();
            }
        }
    }
}
