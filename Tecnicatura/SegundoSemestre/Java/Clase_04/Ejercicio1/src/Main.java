//Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar
//la suma de todos los números introducidos.
import javax.swing.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int suma = 0;
        int numero;

//    do {
//        System.out.println("Digite un número:");
//        numero = entrada.nextInt();
//        suma += numero;
//    } while (numero != 0);
//
//    System.out.println("La suma de todos los números es:"+ suma);


        do{
            String input = JOptionPane.showInputDialog("Digite un número:");
            numero = Integer.parseInt(input);
            suma += numero;
        } while (numero != 0);

        JOptionPane.showMessageDialog(null,"La suma de los números es:"+suma);
    }
}