package utn.practica.Clase03;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio5JuegoAdivinarNumeroJOPtion {
    public static void main(String[] args) {
        /**Ejercicio 5: Realizar un juego para adivinar un n° para
         * ello genera un n° aleatorio entre 0-100, y luego ir pidiendo
         * números indicando "es mayor" o "es menor" según sea mayor o menor
         * con respecto a N . El proceso termina cuando el usuario acierta
         * y mostramos el n° de intentos hechos */

        int numero, aleatorio , conteo = 0 ;
        aleatorio = (int) (Math.random() * 100); //esto genera un n° aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un n° mayor");
            }else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un n° menor");
            }else{
                JOptionPane.showMessageDialog(null,"¡¡¡FELICIDADES!!! Has adivinado el número");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el número en: " + conteo + " intentos");
    }
}
