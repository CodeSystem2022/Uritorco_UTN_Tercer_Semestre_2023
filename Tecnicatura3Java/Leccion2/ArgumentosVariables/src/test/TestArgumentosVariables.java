package test;

public class TestArgumentosVariables {

    public static void main(String[] args) {
        imprimirNumeros(3,4,5);
        imprimirNumeros(1,2);
        variosParametros("Juan","Perez",7,8,9);
    }
    private static void variosParametros(String nombre,String apellido, int ...numeros){
        //Podemos recibir, dentro de un metodo, mas parametros
        System.out.println("Nombre: "+nombre+ "Apellido: "+apellido);
        imprimirNumeros(numeros);
        //Si hay mas parametros dentro del metodo el argumento variable va a ir al final
}
    private static void imprimirNumeros(int... numeros){
//Esta variable se va a convertir en un arreglo de tipo entero. Los (...) Nos indica que la cant de arguemntos
//es inespecifica. Por eso no se la cant de elementos que voy a recibir
//En los argumentos variables no es necesario saber cuantos argumentos voy a pasar al metodo
for (int i = 0; i < numeros.length; i++) //for + tab se forma todo
//Mientras el valor sea mejor a la longitud del arreglo que estamos recibiendo a traves de los argumentos variables
     {System.out.println("Elementos: "+numeros[i]);
            
}
    }
}


