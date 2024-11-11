//  Clase 6
//  Video 7
//Paso por referencia
package pasoporreferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: "+persona1.nombre);
        //  Video 8
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = null;  //if null
        Persona persona2 = new Persona();   //else
        persona2 = cambiarElValor(persona2);    
        System.out.println("El nuevo valor del objeto es: "+persona2.nombre);   //else
    }
    
    public static void cambiarValor(Persona persona){ // Parametro o paso por referencia
        persona.nombre = "Maria";
        //return;   //Lo pone automaticamente, si lo agregamos no genera error
        //El return no es requerido cuando esta dentro de un metodo void (que no retorna nada).
    }
    //  Video 8
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("Valor de persona es invalido : Null");
            return null;
        }
        else{
            persona.nombre = "Monica";
            return persona;     
        }
    }
}
