
package test;

public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        /*Cada uno de los tipo primitivos tienen una clase en java asociada como clase WRAPPER-es decir, clase envolvente de
        /tipo primitivo.
        CLASES ENVOLVENTES DE TIPOS PRIMITIVOS
        INT=La clase envolvente es Integer
        Las clases tienen atributos y metodos. Esa es la diferencia entre un primitivo y el que va a trabajar con la clase
        INTEGER
        LONG=La clase envolvente es Long
        FLOAT=La clase envolvente es Float
        DOUBLE=La clase envolvente es Double
        BOOLEAN=La clase envolvente es boolean
        BYTE=La clase envolvente es byte
        CHAR=La clase envolvente es char
        */
        int enteroPrim=10; //Tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        int entero=10; //Tipo object con la clase Integer
        System.out.println("entero = " + entero.doubleValue()); //Autoboxing
        
        
        int entero2=entero; /*Estamos haciedno unboxing. Se extrae la literal del objeto entero y se asigna a nuetra 
        y el valor que contenia era un objeto pero ahora paso a estar dentro de una variable primitiva. Estamos haciendo
        lo contrario a lo que hicimos antes 
        */
        System.out.println("entero2 = " + entero2);
        
        
    }
    
}
