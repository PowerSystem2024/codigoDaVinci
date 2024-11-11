/*
Ejercicio 11: Leer 5 elementos numericos que se introduciran ordenados de forma
creciente. Estos los guardaremos en una tabla de tamanio 10. Leer un numero N,
e insertarlo en el lugar adecuado para que la tabla continue ordenada.
*/
package arreglos_ejercicio_11;

import java.util.Scanner;

public class Arreglos_Ejercicio_11 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int [] tabla = new int [10];
        boolean creciente = true;
        int numero,sitio_num= 0 , j=0;
        
        do {
            System.out.println("Ingrese los numeros de forma creciente: ");
            for (int i = 0; i < 5; i++) {
                System.out.print("Numero de la pocision "+(i+1)+": ");
                tabla[i] = entrada.nextInt();
            }
        
            for (int i = 0; i < 4; i++) {
                if (tabla[i] < tabla[i+1]) {//Creciente 1,2,3
                    creciente = true;
                }
                if (tabla[i] > tabla[i+1]){
                    creciente = false;
                    break;
                }
            }
        
            if (creciente == false) {
                System.out.println("\nEl arreglo no esta ordenado en forma creciente");
            }
        } while (creciente == false);
        
        System.out.print("Digite un numero a insertar: ");
        numero = entrada.nextInt();
        
        //Esto es para darnos cuenta en que posicion va el numero
        while(tabla[j]<numero && j<5){
            sitio_num++;
            j++;
        }
        
        //Por ultimo, trasladamos una posicion en el arreglo a los elementos que van detras de numero
        for(int i=4;i >= sitio_num;i--){
            tabla[i+1] = tabla[i];
        }
        
        //Insertamos el numero
        tabla[sitio_num] = numero;
        
        System.out.print("\nEl arreglo queda: ");
        for (int i = 0; i < 6; i++) {
            System.out.print(tabla[i]+" - ");
        }
        System.out.print("");
    }
}
