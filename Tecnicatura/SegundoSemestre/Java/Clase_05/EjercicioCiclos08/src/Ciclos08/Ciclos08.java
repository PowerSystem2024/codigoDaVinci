/*
Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N
*/
package Ciclos08;

import java.util.Scanner;

public class Ciclos08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero:");
        int N = Integer.parseInt(entrada.nextLine());
        var contador = 0;
        for (contador = 1; contador <= N; contador ++){ // for (contador = (donde empieza) ; contador (donde termina) ; contador (como debe itera. de a 1 + , 2 negativos, etc)
            System.out.println(contador);
        }
    }
}
