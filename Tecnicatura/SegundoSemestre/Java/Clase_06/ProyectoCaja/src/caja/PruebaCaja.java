/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las especificaciones
mostradas a continuacion.
La formula es: volumen = ancho * alto * profundidad
*/
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        //Variable locales
        int medidaAncho = 3;    //Valores ingresados en codigo duro
        int medidaAlto = 2;
        int medidaProfundo = 6;
        //Caja 1
        Caja volumenCaja1 = new Caja();
        volumenCaja1.alto = medidaAlto;
        volumenCaja1.ancho = medidaAncho;
        volumenCaja1.profundidad = medidaProfundo;
        int resultadoVolumen = volumenCaja1.volumen();
        System.out.println("El volumen de la caja 1 es: "+resultadoVolumen);
        //Caja 2
        Caja volumenCaja2 = new Caja(4,4,4);
        resultadoVolumen = volumenCaja2.volumen();//Llamamos al metodo
        System.out.println("El volumen de la caja 2 es: "+resultadoVolumen);
    }
}
