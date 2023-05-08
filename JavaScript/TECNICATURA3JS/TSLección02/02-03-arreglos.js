
//Creación de Array o arreglos
//let autos = new Array('Ferrari', 'Renault', 'BMW'); esta es la sintaxis vieja
const autos = ['Ferrari','Renault','BMW'];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i]);
}

// Modificamos los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores
autos.push('Audi');
console.log(autos);

//Otras forma de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);

//Tercera forma de agregar elementos teniendo CUIDADO
autos[6] = 'Renault';
console.log(autos);

// Como preguntar si es una Array o Arreglo
console.log(Array.isArray(autos)); //Devuelve un booleano


console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase Array
