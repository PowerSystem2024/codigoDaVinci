/*
Ejercicio 9: Pedir el dia,mes y año de una fecha e 
indicar si la fecha es correcta. Suponiendo que
todos los meses son de 30 dias
*/
package Ciclos09;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el dia (De forma numerica): ");
        int dia = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el mes (De forma numerica): ");
        int mes = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el año (De forma numerica): ");
        int anio = Integer.parseInt(entrada.nextLine());
        if (dia >= 1 && dia <= 30){
            if (mes >= 1 && mes <= 12){
                if (anio >= 1 && anio <= 2024){System.out.println("La fecha ingresada ("+dia+"/"+mes+"/"+anio+") es correcta");
                }
                else{System.out.println("El año ingresado es incorrecto");
                }
            }
            else{System.out.println("El mes ingresado es incorrecto");          
            }
        }
        else{System.out.println("El dia ingresado es incorrecto");            
        }
    }    
}
