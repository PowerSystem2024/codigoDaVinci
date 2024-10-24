package utn.practica.Clase03;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio3LeerNumeroJOptionaPane {
    public static void main(String[] args) {
/**Ejercicio 3: Leer númneros hasta que se introduzca un cero para cada uno indicar si es par o impar */
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca un número: "));

        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número: " + numero + " es par");
            }else{
                JOptionPane.showMessageDialog(null,"El número: " + numero + " es impar");
            }
            //si no pidiera que ingresen otro número , el ciclo sería infinito si el n° ingresado es <> de 0
            System.out.println("Digite otro número");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Introduzca otro número: "));
        }
        JOptionPane.showMessageDialog(null,"Fin del programa, introdujiste el número: " + numero);
    }
    }

