/*
Ejercicio 1:leer un numero y mostrar su cuadrado, repetir hasta que se introduzca un numero negativo
*/
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio1 {
    public static void main(String[] args) {
        
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        while(numero >= 0){
            cuadrado = (int)Math.pow(numero, 2);
            JOptionPane.showMessageDialog(null, "El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El programa a finalizado por ingresar un numero ngativo");
    }
}
