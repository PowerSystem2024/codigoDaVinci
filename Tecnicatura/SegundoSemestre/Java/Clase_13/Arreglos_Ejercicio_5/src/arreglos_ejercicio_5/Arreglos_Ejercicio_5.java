/*
Ejercicio 5: Leer por teclado dos tablas de 10 numeros
enteros y mezclarias en un tercera de la forma: el 1 de 
A, el 1 de B, el 2 de A, el 2 de B, etc.
*/
package arreglos_ejercicio_5;

import java.util.Scanner;

public class Arreglos_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int[] a = new int [10];
        int[] b = new int [10];
        int[] c = new int [20];
        int contadorA = 0;
        int contadorB = 0;
        
        System.out.println("Ingrese los numeros de la tabla a:");
        for (int i = 0; i < 10; i++) {
            a[i] = entrada.nextInt();
        }
        
        System.out.println("Ingrese los numeros de la tabla b:");
        for (int i = 0; i < 10; i++) {
            b[i] = entrada.nextInt();
        }
        
        //Agregamos los numeros a la lista c
        System.out.println("Mostramos la lista c:");
        for (int i = 0; i < 20; i++) {
            if (i % 2 == 0){
                c[i] = a[contadorA];
                contadorA++;
            }
            else{
                c[i] = b[contadorB];
                contadorB++;
            }
        }
        
        for (int i = 0; i < 20; i++) {
            System.out.println(c[i]);
        }
    }
}
