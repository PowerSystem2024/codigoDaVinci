//  Clase 7
//  Video 7
package dominio;

public class Persona {
    //Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    //Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    
    //Metodos get y set
    public String getNombre(){
        return nombre;
    }
    
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    
    public double getSueldo(){
        return sueldo;
    }
    
    public void setSueldo(double sueldo){
        this.sueldo = sueldo;
    }
    
    public boolean isEliminado(){ //Usa is en lugar de get porque is: True or False. Siempre se usa para los booleanos
        return eliminado;
    }
    
    public void setEliminado(boolean eliminado){
        this.eliminado = eliminado;
    }
    
    //  Clase 8
    //  Video 3
    public String toString(){   //Convierte en una cadena cada atributo
        return "Persona [ nombre : "+this.nombre+
                ", sueldo: "+this.sueldo+
                ", eliminado: "+this.eliminado+"]";
    }
}
