
package Clases;

public class PruebaPErsona {
    public static void main(String[] args) {        
        Persona persona1 = new Persona();   //Llamamos al constructor.Es en el unico lugar que se lo pone al new + constructor
        persona1.nombre = "Santiago";       //El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Seleme";        
        persona1.obtenerInformacion();        
        
        Persona persona2 = new Persona();         
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();        
        persona2.nombre = "Ariel";
        persona2.apellido = "Betancud";
        persona2.obtenerInformacion();
    }
}
