/*
Ejercicio 11: Diseniar un programa que muestre el producto
de los 10 primeros numeros impares
Hacerlo con JOptionPane
*/
package Ciclos11;

import javax.swing.JOptionPane;

public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
//        int contador = 1;        
//        int numero = 0;
//        while(contador <= 10){
//            if (numero % 2 == 1){
//                JOptionPane.showConfirmDialog(null,producto+" * "+numero+" = "+(numero*producto));
//                producto *= numero;
//                contador ++;
//            }
//            numero ++;
//        }
        for (int i = 1; i<=20 ; i+=2){ //El aumento apunta a solo ir por los impares
            producto *= i;
        }
        JOptionPane.showConfirmDialog(null,"Este es el producto de los primeros 10 impares = "+producto);
    }
}
