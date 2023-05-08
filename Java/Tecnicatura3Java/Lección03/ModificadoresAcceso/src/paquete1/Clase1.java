
package paquete1;

public class Clase1 {
    public String atributoPublic = "Valor atributo"; 
    protected String atributoProtected = "Ariel atributo protected";    
    public Clase1(){
        System.out.println("Constructor public");
}
    
    protected Clase1(String atributoPublic){
        System.out.println("Constructor protected");
    }
 
    public void metodoPublico(){
        System.out.println("Método public");
    }
    
    
     public void metodoProtected(){
        System.out.println("Método protected");
    }
}
