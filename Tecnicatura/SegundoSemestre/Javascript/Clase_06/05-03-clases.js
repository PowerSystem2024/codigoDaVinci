//let persona3 = new Persona("Carla", "Ponce"); esto no se debe hacer: Persona in not defined

class Persona{ //clase padre

    static contadorPersona = 0; //Atributo static
    //email = "valor default email"; //Atributo no static

    static get MAX_OBJ(){ // Este metodo simula una constante
        return 5;
    }

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersona < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersona;
        }
        else{
            console.log("Se ha superado el maximo de objetos permitidos");
        }
        //console.log("Se incrementa el contador: "+Persona.contadorObjetosPersona);
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

    nombreCompleto(){
        return this.idPersona+" "+this.nombre+" "+this.apellido;
    }
    //Sobreescribiendo el metodo de la clase padre (Object)
    toString(){ //Regresa un String
        // Se aplic el polimorfismo que significa = muliples formas en tiempo de ejecucion
        //El metodo que se ejecuta si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log("Saludos desde este metodo static");
    }

    static saludar2(persona){
        console.log(persona.nombre+" "+persona.apellido);
    }
}

class Empleado extends Persona{ //clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido)
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    
    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+", "+this._departamento
    }
}

let persona1 = new Persona("Martin", "Perez");
console.log(persona1.nombre);
persona1.nombre = "Juan Carlos";
console.log(persona1.nombre)
//console.log(persona1);
console.log(persona1.apellido);
persona1.apellido = "Llugany"
console.log(persona1.apellido);
let persona2 = new Persona("Carlos", "Lara")
console.log(persona2.nombre);
persona2.nombre = "Maria Laura";
console.log(persona2.nombre)
console.log(persona2.apellido)
//console.log(persona2);
persona2.apellido = "Martinez"
console.log(persona2.apellido);


let empleado1 = new Empleado("Maria", "Gimenez", "Sistema");
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de aceder a atributos y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());

//persona1.saludar(); no se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorPersona);
console.log(Empleado.contadorPersona);

console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.email); No puede acceder desde la clase

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersona);
let persona3 = new Persona("Carla", "Pertosi");
console.log(persona3.toString());
console.log(Persona.contadorPersona);

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; No se puede modificar, ni alterar
console.log(Persona.MAX_OBJ);

let perosna4 = new Persona("Franco", "Diaz");
console.log(perosna4.toString());
let perosna5 = new Persona("Liliana", "Paz");
console.log(perosna5.toString());






