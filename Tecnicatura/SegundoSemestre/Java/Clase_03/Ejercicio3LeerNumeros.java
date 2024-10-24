package utn.practica.Clase03;

import java.util.Scanner;

public class Ejercicio3LeerNumeros {
    /**Ejercicio 3: Leer úmeros hasta que se introduzca un cero
     * para cada uno indicar si es par o impar
     * Primero lo haremos con la clase Scanner*/
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un número");
        numero = Integer.parseInt(entrada.nextLine());

        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El número: " + numero + " es par");
            }else{
                System.out.println("El número: " + numero + " es impar");
            }
            //si no pidiera que ingresen otro número , el ciclo sería infinito si el n° ingresado es <> de 0
            System.out.println("Digite otro número");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Fin del programa, introdujiste el número: " + numero);
    }
}
