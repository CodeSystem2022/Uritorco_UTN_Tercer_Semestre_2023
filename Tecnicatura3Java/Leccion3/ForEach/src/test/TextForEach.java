
package test;

import domain.Persona;

public class TextForEach {
    public static void main(String[] args) {
        int edades[]={5,6,7,8,9}; //Sintaxis resumida
        for (int edad:edades){ //Sintaxis del Foreach
            System.out.println("edad= " + edad);
            
    
}
        Persona personas[]={new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz")};
        
        //ForEACH
        for(Persona persona: personas){
            System.out.println("persona = " + persona); //Aca esta la variable de tipo objeto para recorrer todo el arreglo
            
        }
        
    }
    
}
