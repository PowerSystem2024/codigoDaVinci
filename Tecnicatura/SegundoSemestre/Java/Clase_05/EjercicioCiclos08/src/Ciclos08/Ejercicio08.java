/*
Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N
*/
package Ciclos08;

import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args) {
        int N = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        var contador = 0;
        for (contador = 1; contador <= N; contador ++){ // for (contador = (donde empieza) ; contador (donde termina) ; contador (como debe itera. de a 1 + , 2 negativos, etc)
            JOptionPane.showMessageDialog(null, contador);
        }
    }
}