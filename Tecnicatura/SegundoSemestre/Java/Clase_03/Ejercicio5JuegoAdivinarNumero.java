package utn.practica.Clase03;

import java.util.Scanner;

public class Ejercicio5JuegoAdivinarNumero {
    public static void main(String[] args) {
        /**Ejercicio 5: Realizar un juego para adivinar un n° para
         * ello genera un n° aleatorio entre 0-100, y luego ir pidiendo
         * números indicando "es mayor" o "es menor" según sea mayor o menor
         * con respecto a N . El proceso termina cuando el usuario acierta
         * y mostramos el n° de intentos hechos */

        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio , conteo = 0 ;
        aleatorio = (int) (Math.random() * 100); //esto genera un n° aleatorio
        do{
            System.out.println("Digite un n°");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("Digite un n° mayor ");
            }else if(numero > aleatorio){
                System.out.println("Digite un n° menor");
            }else{
                System.out.println("¡¡¡FELICIDADES!!! Has adivinado el número");
            }
            conteo++;
        }while(numero != aleatorio);
        System.out.println("Adivnaste el número en :" + conteo + " intentos");

    }
}
