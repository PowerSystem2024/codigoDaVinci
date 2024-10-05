/*
Ejercicio 2: leer un numero e indicar si es positivo o onegativo
el proceso se repetira hasta que se introduzca un cero
*/
package Ejercicio2;

import javax.swing.JOptionPane;

public class Ejercicio0202 {
    public static void main(String[] args) {
        
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero ingresado finaliza el programa");
    }
}

