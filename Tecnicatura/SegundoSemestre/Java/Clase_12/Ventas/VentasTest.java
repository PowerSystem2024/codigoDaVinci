package utn.practica.Clase_12.Ventas;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);

        Orden orden1 = new Orden();
        orden1.mostrarOrden(); //La orden esta vacia

        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        System.out.println("");

        //Tarea:
        //Crear mas objetos de tipo Producto
        //Crear mas objetos de tipo Orden
        Producto producto3 = new Producto("Cadena de oro", 999000.00);
        Producto producto4 = new Producto("Gorra cerrada", 23999.00);
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.mostrarOrden();
        System.out.println("");

        Producto producto5 = new Producto("Camisa negra", 30000.00);
        Producto producto6 = new Producto("Tapado de cuero", 49999.00);
        Producto producto7 = new Producto("Lentes de sol", 10000.00);
        Producto producto8 = new Producto("Pendientes de diamantes", 75000.00);
        Producto producto9 = new Producto("Calzoncillos calvin klein", 7499.00);
        Producto producto10 = new Producto("Zapatos de cuero", 24999.00);
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto1);
        orden3.agregarProducto(producto2);
        orden3.agregarProducto(producto3);
        orden3.agregarProducto(producto4);
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto4);
        orden3.mostrarOrden();
    }
}
