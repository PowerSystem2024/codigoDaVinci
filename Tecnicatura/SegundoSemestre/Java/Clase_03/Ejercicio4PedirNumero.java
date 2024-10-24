package utn.practica.Clase03;

import java.util.Scanner;

public class Ejercicio4PedirNumero {
    public static void main(String[] args) {
        /**Ejercicio 4: Pedir números hasta que se teclee uno
         * negativo y mostrar cuántos números se han introducido*/
        Scanner entrada = new Scanner(System.in);
        var contador = 0;
        System.out.println("Digite un número ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero > 0){
            contador++;
            System.out.println("Ingrese otro número");
         numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("La cantidad de números ingresados es : " + contador);

    }
}
