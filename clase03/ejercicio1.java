// Ejercio 1
/*
 Facturador accede a Cliente y luego directamente a Direccion 
para obtener la ciudad. Si la estructura de Direccion cambia (ej. 
se añade un idioma o se separa código postal), Facturador se rompe. 
*/
// Corrección
public class Cliente {
    private Dirección direccion;

    public String getCiudad() {
        return this.direccion.GetCiudad();
    }
}

public class Facturador { 
    public void imprimirFactura(Cliente cliente) { 
        // Depende de la estructura interna de Direccion 
        //String ciudad = cliente.getDireccion().getCiudad(); 

        // Con esto solo se accede a lo que se necesita 
        System.out.println("Ciudad: " + cliente.getCiudad()); 
    } 
} 
