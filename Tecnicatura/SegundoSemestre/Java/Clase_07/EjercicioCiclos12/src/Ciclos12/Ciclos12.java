/*
Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con las dos clase, Scanner y JOptionPane
*/
package Ciclos12;

//import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        //System.out.println("Digite un numero: ");        
        //int numero = Integer.parseInt(entrada.nextLine());
        
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero:")); //JOption
        
        int factorial = 1;
        for(int i = numero ; i >= 1; i--){
            factorial *= i;
        }
        //System.out.println("El factorial de "+numero+" es: "+factorial);
        
        JOptionPane.showMessageDialog(null,"El factorial de "+numero+" es: "+factorial); //JOption
    }
}
