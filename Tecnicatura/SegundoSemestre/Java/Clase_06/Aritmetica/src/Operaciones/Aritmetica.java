
package Operaciones;

public class Aritmetica {
    //  Clase 4
    //Atributos de la clase
    int a;
    int b;
    
    //  Clase 6
    //  Video 1
    //El constructor es un metodo especial
    public Aritmetica(){    //Constructor 1 vacio
        System.out.println("Se esta ejecutando este constructor numero uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){//Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos");
    }
    
    //Metodo
    public void sumarNumeros(){ //Cuerpo de la clase
        int resultado = a + b;       //Variables locales, se crean dentro de la clase y luego de terminado el programa se eliminan
        System.out.println("resultado = "+resultado);   // Este metodo no retorna nada, solo muestra por pantalla
    }
    //  Clase 5
    //  Video 2
    public int sumarConRetorno(){   //Metodo con un retorno de tipo entero
        // Una forma es la siguiente:
        // int resultado = a + b;
        // return resultado;
        
        // O si tambien funciona:
        return this.a + this.b;   // Utilizamos los mismo atributos que el metodo anterior
    }    
    // Video 4
    // Modificador de acceso(public) Tipo de retorno(int) Identidicador(nombreDeMetodo) (parametros) {...
    public int sumarConArgumentos(int a, int b){
        // Video 6 - operador this (ayuda a diferenciar los atributos de los argumentos)
        this.a = a;  // El argumento a se asigna al atributo this.a
        this.b = b;  // atributo = variable
        // Lo que hace es que cambia el valor de los atributos ('a' y 'b') solo durante el proceso de este metodo por el de los
        // argumentos ingresados en la invocacion del metodo en PruebaAritmetica
        //return a + b;
        
        // Video 5
        return this.sumarConRetorno();   // Se puede llamar un metodo desde otro, solo estando en la misma Class
        
        
    }
}
