//  Clase 11 Parte 1
//  Video 4

public class Persona {
    private String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    //  Video 5

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}'+", "+super.toString();//este toString es de la clase padre Object
    }
    
}
