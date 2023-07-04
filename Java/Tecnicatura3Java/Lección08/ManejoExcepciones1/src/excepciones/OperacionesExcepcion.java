package excepciones;

public class OperacionesExcepcion extends RuntimeException {
    // Constructor
    public OperacionesExcepcion(String mensaje) {
        super(mensaje);
    }
}
