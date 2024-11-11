/*
Ejercicio 4: Leer 10 numeros enteros, guardarlos en un 
arreglo. Debemos mostrarlos en el siguiente orden: el primero,
el utlimo, el segundo, el penultimo, el tercero, etc
*/
package arreglos_ejercicio_4;

import java.util.Scanner;

public class Arreglos_Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int [] numeros = new int[10];
        int primeros = 0;
        int ultimos = 9;
        
        for (int i = 0; i < 10; i++) {
            System.out.println("Digite un numero entero: ");
            numeros[i] = entrada.nextInt();
        }
        
        //Mostramos los numeros con el patron que nos piden
        System.out.println("Mostramos los numeros: ");
        for (int i = 0; i < 10; i++) {
            if (i % 2 == 0){
                System.out.println(numeros[primeros]);
                primeros ++;
            }
            else{
                System.out.println(numeros[ultimos]);
                ultimos--;
            }
        }
    }
}
