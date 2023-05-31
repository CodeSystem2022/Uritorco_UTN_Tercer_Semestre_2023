
package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Dia 1: "+Dias.LUNES); //Podes acceder a los atributos es como un elemento de enumeracion pero 
        //pero recordar que este atributo es estatico y publico
        //Cada uno de los valores de enumeracion son cadenas
        //indicarDiaSemana(Dias.LUNES); //Las enumeraciones se tratan como cadenas
        //Ahora no se deben utilizar comillas, se accede a traves del operador de punto   
        System.out.println("Contiente No.4: "+Continentes.AMERICA);
        //¿COMO SABER CUANTOS PAISES TIENE ESTE CONTINENTE?
        System.out.println("No. de paieses en el 4to continente: "+Continentes.AMERICA.getPaises());
        System.out.println("No de habitantes en el 4to contienente: "+Continentes.AMERICA.getHabitantes());
        System.out.println("No. de paieses en el 1er continente: "+Continentes.AFRICA.getPaises());
        System.out.println("No de habitantes en el 1er contienente: "+Continentes.AFRICA.getHabitantes());
        System.out.println("No. de paieses en el 2do continente: "+Continentes.EUROPA.getPaises());
        System.out.println("No de habitantes en el 2do contienente: "+Continentes.EUROPA.getHabitantes());
        System.out.println("No. de paieses en el 3ER continente: "+Continentes.ASIA.getPaises());
        System.out.println("No de habitantes en el 3ER contienente: "+Continentes.ASIA.getHabitantes());
        System.out.println("No. de paieses en el 5TO continente: "+Continentes.OCEANIA.getPaises());
        System.out.println("No de habitantes en el 5TO contienente: "+Continentes.OCEANIA.getHabitantes());
      
    }
    private static void indicarDiaSemana(Dias dias){ //Vamos utilizar la enumeracion para pasar un parametro a nuestro 
        //metodo y posteriormente este metodo va a imprimir que dia de la semana es 
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
                break;
            
            //Agregar default en el swicth
                
        }
}
}