package utn.practica.Clase_12.Ventas;

public class Orden {
    private int idOrden;
    private Producto productos[]; // Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10; // Sintaxis y norma de escritura de un constante en Java

    //Constructor vacio
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }

    //  VIDEO 4
    public void agregarProducto(Producto producto){
        //Validacion para la cantidad maxima de productos en una orden
        if(this.contadorProductos < Orden.MAX_PRODUCTOS){
            this.productos[this.contadorProductos++] = producto;
        }
        else{
            System.out.println("Se ha superado el maximo de productos: "+Orden.MAX_PRODUCTOS);
        }
    }

    //  VIDEO 5
    public double calcularTotal(){
        double total = 0; // Variable temporal
        for (int i = 0; i < this.contadorProductos; i++) {
//            Producto producto = this.productos[i];
//            total += producto.getPrecio();
            total += this.productos[i].getPrecio();
        }
        return total;
    }

    //  VIDEO 6
    public void mostrarOrden(){
        System.out.println("Id Orden: "+this.idOrden);
        double totalOrden = this.calcularTotal();
        System.out.println("El total de la orden es: $"+totalOrden);
        System.out.println("Productos de la orden: ");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);
        }
    }
}
