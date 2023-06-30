//let persona3 =new Persona("Carla", "Ponce"); esto no se debe hacer: Persona is not defined

class Persona{  // Clase padre


    static contadorPersonas = 0;

    static get MAX_OBJ() {
        return 5;
    } 

    constructor (nombre, apellido){
        this._nombre = nombre;
        this.apellido = apellido;
        if (Persona.contadorPersonas < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersonas;
        } else {
            console.log("Se ha superado el máximo de objetos permitidos.");
        }
    }
    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto() {
        return this._nombre + " " + this.apellido;
     }
     
     //Sobrescritura
     toString() {
         //El método depende de si es referencia base o derivada. Aplica polimorfismo.
         return this.nombreCompleto();
     }

     static saludar() {
        console.log("Saludos desde este método Static");
     }

     static saludar2() {
        console.log(persona.nombre + " " + persona.apellido);
     }

}

class Empleado extends Persona {  //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    
    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    nombreCompleto() {
       // return super.nombreCompleto() + ", " + this._departamento;
       return super.nombreCompleto() + ", " + this._departamento;
    }
}


//Clase hija
let persona1 = new Persona("Martín", "Pérez");
console.log(persona1.nombre)
persona1.nombre = "Juan Carlos";
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona("Carlos", "Lara");
console.log(persona2.nombre);
persona2.nombre = "María Laura";    //console.log(persona2.nombre);
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado("María", "Gimenez", "Sistemas");
console.log(empleado1);
console.log(empleado1.nombreCompleto());

console.log(empleado1.toString());
console.log(persona1.toString());

Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

console.log(person1.email);
console.log(empleado1.email);

let persona3 = new Persona("Carla", "Pertosi");
console.log(persoan3.toString());

console.log(Persona.MAX_OBJ);

let persona4 = new Persona("Franco", "Diaz");
console.log(persona4.toString());

let persona5 = new Persona("Liliana", "Paz");
console.log(persona5.toString());