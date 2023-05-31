
package domain;
//Tenemos bloques de inicializacion estaticos y no estaticos
//Los bloques se van a ejecutar antes de constructor y amtes que cualquier bloque no estatico
//El bloque estatico se ejecuta cuando se carga la clase en memoria

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ //Bloque de inicializacion estatico
        System.out.println("Ejecucion del bloque estatico");
        ++Persona.contadorPersonas;
        //idPersona=10; No es un atributo estatico por eso tenemos ese error
          
}
    { ///Bloque de inicializacion NO ESTATICO O CONTEXTO DINAMICO
        System.out.println("Ejecucion del bloque NO ESTATICO");
        this.idPersona=Persona.contadorPersonas++; //Incrementamos el atributo
        
    }
    public Persona(){
        System.out.println("Ejecucion del constructor");
    }
    public int getidPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}
