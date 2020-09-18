package com.calculadora.basic;

import java.util.Scanner;

public class Calcular {

	public static void main(String[] args) {
		/*Programa que realiza uma operação com dois números do tipo
		 * double. As operações disponíveis são: adição, subtração, multiplicação
		 * e divisão. Além dessas, pode-se escolher também potenciação e
		 * radiciação.
		 * 
		 */
		
		//Variáveis importantes para o programa
		double n1 = 0, n2 = 0;
		int amount = 0, choice;
		Scanner entrada = new Scanner(System.in);
		
		//Mostrando ao usuário as opções disponíveis a ele
		System.out.println("1 - ADIÇÃO");
		System.out.println("2 - SUBTRAÇÃO");
		System.out.println("3 - MULTIPLICAÇÃO");
		System.out.println("4 - DIVISÃO");
		System.out.println("5 - POTENCIAÇÃO");
		System.out.println("6 - RADICIAÇÃO");
		
		//Pedindo ao usuário a escolha da operação ou outro tipo de ação matemática
		
		System.out.println("Escolha: ");
		choice = entrada.nextInt();
		
		//Impedindo que o usuário insira números fora do intervalo das escolhas possíveis
		while (choice > 6 || choice < 1) {
			System.out.println("O número inserido não corresponde a nenhuma opção existente! Insira outro!");
			System.out.println("Escolha: ");
			choice = entrada.nextInt();
		}
		
		//Pedindo os números ao usuário
		
		System.out.println("Primeiro número: ");
		n1 = entrada.nextDouble();
		System.out.println("Segundo número: ");
		n2 = entrada.nextDouble();
		
		//Estrutura condicional para calcular os resultados das operações pedidas
		
		if (choice == 1) {
			double total = n1 + n2;
			//Exibindo a operação e o resultado de acordo com o sinal do segundo número
			if (n2 < 0) {
				System.out.printf("\n %.2f + (%.2f) = %.2f", n1, n2, total);
			} else {
				System.out.printf("\n %.2f + %.2f = %.2f", n1, n2, total);
			}
		} else if (choice == 2) {
			double difer = n1 - n2;
			//Exibindo a operação e o resultado de acordo com o sinal do segundo número
			if (n2 < 0) {
				System.out.format("%.2f - (%.2f) = %.2f", n1, n2, difer);	
			} else {
				System.out.format("%.2f - %.2f = %.2f", n1, n2, difer);
			}
		} else if (choice == 3) {
			double produto = n1 * n2;
			//Exibindo a operação e o resultado de acordo com o sinal do segundo número
			if (n2 >= 0) {
				System.out.format("%.2f * %.2f = %.2f", n1, n2, produto);
			} else {
				System.out.format("%.2f * (%.2f) = %.2f", n1, n2, produto);
			}
		} else if (choice == 4) {
			
			//Impedindo que o usuário insira zero como o divisor da divisão para se evitar problemas durante a execução do código
			while (n2 == 0) {
				System.out.println("Não existe divisão por zero!");
				System.out.println("Troque o segundo número por outro!");
				System.out.println("Segundo número: ");
				n2 = entrada.nextDouble();
			}
			double quociente = n1 / n2;
			System.out.format("\n %.2f / %.2f = %.2f", n1, n2, quociente);
		} else if (choice == 5) {
			double potencia = Math.pow(n1, n2);
			System.out.format("\n %.2f ^ %.2f = %.2f", n1, n2, potencia);
		} else if (choice == 6) {
			
			//Impedindo que o usuário insira um número negativo como radicando de uma raiz de índice par
			while (n2 % 2 == 0 && n1 < 0) {
				System.out.println("Não existe raiz inteira em um radical de índice par e cujo radicando é negativo!");
				System.out.println("Primeiro número: ");
				n1 = entrada.nextDouble();
				System.out.println("Segundo número: ");
				n2 = entrada.nextDouble();
			}
			
			double raiz = Math.pow(n1, (1/n2));
			System.out.format("\n %.2f ^ (1/%.2f) = %.2f", n1, n2, raiz);
		}
		
		
		

	}

}
