/*
Ejercicio 10: Pedir 10 numeros y escribir la suma
total
Hacerlo con la clase Scanner y JOptionPane
*/
package Ciclos10;

import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        int contador = 0;
        int iteraciones = 10;
        int suma = 0;
        for (contador = 1; contador <= iteraciones ; contador++){
            suma += Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:"));
        }
        JOptionPane.showMessageDialog(null,"La suma de los numeros es: "+suma);
    }
}
