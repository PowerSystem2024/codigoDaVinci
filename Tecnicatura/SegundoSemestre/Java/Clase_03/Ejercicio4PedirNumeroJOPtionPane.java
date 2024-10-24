package utn.practica.Clase03;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio4PedirNumeroJOPtionPane {
    public static void main(String[] args) {
        /**Ejercicio 4: Pedir números hasta que se teclee uno
         * negativo y mostrar cuántos números se han introducido*/
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
        var contador = 0;
        while (numero > 0){
            contador++;
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));

        }
       JOptionPane.showMessageDialog(null, "La cantidad de números ingresados es : " + contador);
    }
}
