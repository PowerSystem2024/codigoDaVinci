//Ejercicio 7: Pedir números hasta que se introduzca uno negativo y calcular la media.
import java.util.Scanner;
import javax.swing.JOptionPane;
public class Main {
    public static void main(String[] args) {
//    Scanner entrada = new Scanner(System.in);

        int suma = 0, contador = 0;
        int numero;

//    while (true) {
//        System.out.println("Digite un número:");
//        numero = entrada.nextInt();
//
//        if (numero < 0) {
//            break;
//        }
//
//        suma += numero;
//        contador ++;
//    }
//
//    if (contador > 0){
//        double media = (double) suma / contador;
//        System.out.println("La media de los números introducidos es: "+media);
//    } else {
//        System.out.println("No se introdujeron números válidos");
//    }

        while (true) {
            String input = JOptionPane.showInputDialog("Digite un número:");
            numero = Integer.parseInt(input);

            if (numero < 0) {
                break;
            }

            suma += numero;
            contador++;
        }

        if (contador > 0){
            double media = (double) suma / contador;
            JOptionPane.showMessageDialog(null, "La media de los números introducidos es: "+media);
        } else {
            JOptionPane.showMessageDialog(null, "No se introdujeron números válidos");
        }

    }
}