/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique:
    variables: Evita cambiar el valor que almacena la variable
    metodos: Evita que se modifiquen la definicion o el comportamiento de un metodo desde una subclase (hija)
    clases: Evita que se creen clases hijas
Otra caracteristica es que normalmente, cuando trabajamos con variables se combinacon el modificador de acceso estatico 
para convertir una variable en una constante, es decir que no se puede modificar su valor, el ejemplo de esto es la clase
Math en la cual todos sus atributos son de tipo static y final, es por esto que la variable pi* se conoce como una constante
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDNI = 123456789;
        System.out.println("miDNI = " + miDNI);
        //miDNI = 987654321; NO SE PUEDE MODIFICAR
        //Persona.CONSTATE_AQUI = 9; //NO se modifica
        System.out.println("Mi atributo constante es: "+Persona.CONSTATE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona; No se puede asignar una nueva referencia
        persona1.setNombre("Ariel Betancud");
        System.out.println("persoan1 nombre: "+persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persoan1 nombre: "+persona1.getNombre());
    }
}
