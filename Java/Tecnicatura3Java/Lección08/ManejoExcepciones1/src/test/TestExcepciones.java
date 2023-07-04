package test;

import static aritmetica.Aritmetica.division;


public class TestExcepciones {
    public static void main(String[] args) {
        int resultado = 0;
        try{
            resultado = division(10, 0);
        } catch (OperacionExcepcion e){
            System.out.println("Ocurrió un error de tipo operacionExcepcion");
            System.out.println(e.getMessege());
        } catch (Exception e){
            System.out.println("Ocurrió un error");
            e.printStackTrace(System.out);//se conoce como pila de excepciones
            System.out.println(e.getMessage());
        }
        finally{
            System.out.println("se revisó la división entre cero");
        }
        System.out.println("La variable de resultado tiene como valor: = " + resultado);
    }
}
