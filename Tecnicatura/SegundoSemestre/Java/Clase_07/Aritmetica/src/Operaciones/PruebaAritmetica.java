// Clase 5
// Video 1
package Operaciones; // Package

public class PruebaAritmetica { // Clase
    public static void main(String[] args) { // Main/Proceso principal
        //  (Clase 6 - Video 2
        var a = 10; //variables locales, El alcance de los atributos atraves de los contructores es mayor que el de una variable local
        int b = 7;  //Memoria stack
        miMetodo(); //Llamamos el metodo nuevo
        //  )
        
        Aritmetica aritmetica1 = new Aritmetica();  // Aritmetica() llama al constructor
        aritmetica1.a = 3;  // Le damos valor a los Atributos
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros(); // Llamamos al metodo, que ya con los valores de a y b ya puede funcionar
        
        // Video 2
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado); // Como este metodo utiliza el mismo constructor, y tambien usamos los mismos
                                                        // atributos nos da el mismo resultado
        // Video 3: Debug paso a paso
        // Video 4
        resultado = aritmetica1.sumarConArgumentos(12, 26); // Argumentos: 12 y 26 
        System.out.println("Resultado usando argumentos = "+resultado);
        
        //  Clase 6
        //  Video 1
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 a= " + aritmetica2.a);
        System.out.println("aritmetica2 b= " + aritmetica2.b);
        //  Video 3
        //aritmetica1 = null; //Limpia la memoria, nunca utilizar esto, no se debe hacer
        //System.gc();    //Metodo para limpiar residuos, no utilizar
        
        //  Clase 7
        //  Video 2
        Persona persona = new Persona("Ariel","Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }
    
    //Clase 6 
    //Video 2
    //Modularidad creamos un nuevo metodo
    public static void miMetodo(){
        int a = 10; //una variable esta limitada
        System.out.println("Aqui hay otro metodo");
    }
}
//  Clase 7
//  Video 1
//Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //Constructor
        super(); //Llamada al constructor de la clase Padre object. Video 5
        // (Video 6
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        //  )
        this.nombre = nombre;
        this.apellido = apellido;
        //  Video 5
        System.out.println("Objeto persona usando this: "+this);
    }
}
//  Video 5
class Imprimir{
    public Imprimir(){
        super(); // el constructor de la clase padre, para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }
}