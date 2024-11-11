/*
Ejercicio 9: Pedir el dia,mes y año de una fecha e 
indicar si la fecha es correcta. Suponiendo que
todos los meses son de 30 dias
*/
package Ciclos09;

import javax.swing.JOptionPane;

public class Ejercicio09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el dia (De forma numerica): "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes (De forma numerica): "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el año (De forma numerica): "));
        if (dia >= 1 && dia <= 30){
            if (mes >= 1 && mes <= 12){
                if (anio >= 1 && anio <= 2024){JOptionPane.showMessageDialog(null,"La fecha ingresada ("+dia+"/"+mes+"/"+anio+") es correcta");
                }
                else{JOptionPane.showMessageDialog(null,"El año ingresado es incorrecto");
                }
            }
            else{JOptionPane.showMessageDialog(null,"El mes ingresado es incorrecto");          
            }
        }
        else{JOptionPane.showMessageDialog(null,"El dia ingresado es incorrecto");            
        }
    }
}
