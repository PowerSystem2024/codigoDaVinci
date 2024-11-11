//  Clase 11 Parte 1
//  Video 1
package test;

public class TestArreglos {
    public static void main(String[] args) {
        int edades[] = new int [3]; // "tipoDato" "nombreObjeto" [] = new "tipoDato" ["cantDatos"]
        //lado izq. declaramos la variable = lado der. instanciamos un objeto tipo object
        
        System.out.println("edades = " + edades);
        
        //  Video 2
        edades[0] = 17;
        System.out.println("edades 0 = " + edades[0]);
        //Tarea: modificar indice 1 y 2
        edades[1] = 21;
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 6;
        System.out.println("edades 2 = " + edades[2]);
        
        //  Video 3
        //edades[3] = 7; // Fuera de rango, error en tiempo de ejecucion
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
        }
       
    }
}
