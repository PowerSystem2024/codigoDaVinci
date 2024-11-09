//  Clase 8 
//  Video 1
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);   //  Video 3
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificamos a traves de los metodos (set)
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; // Ya no se puede utilizar
        
        //Mostramos a traves de los metodos (get)
        //System.out.println("Nombre es: "+persona1.nombre); // Error
        System.out.println("persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        // Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        // e imprimir, luego modificar sus valores y volver a imprimir
        Persona persona2 = new Persona("Abel", 20000000, false);
        System.out.println("persona2 nombre: "+persona2.getNombre());
        System.out.println("persona2 sueldo: "+persona2.getSueldo());
        System.out.println("persona2 booleano: "+persona2.isEliminado());
        persona2.setNombre("Mauro");
        persona2.setSueldo(4500000);
        persona2.setEliminado(true);
        System.out.println("persona2 nombre nuevo: "+persona2.getNombre());
        System.out.println("persona2 sueldo nuevo: "+persona2.getSueldo());
        System.out.println("persona2 booleano nuevo: "+persona2.isEliminado());
        //  Video 3
        System.out.println("persona1 = " + persona1); // persona1 = persona1.toString
    }
}
