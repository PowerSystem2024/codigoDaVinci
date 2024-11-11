/*
Ejercicio 10: Pedir 10 numeros y escribir la suma
total
Hacerlo con la clase Scanner y JOptionPane
*/
package Ciclos10;

import java.util.Scanner;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int contador = 0;
        int iteraciones = 10;
        int suma = 0;
        for (contador = 1; contador <= iteraciones ; contador++){
            System.out.println("Digite un numero: ");
            suma += Integer.parseInt(entrada.nextLine());
        }
        System.out.println("La suma de los numeros es: "+suma);
    }
}
