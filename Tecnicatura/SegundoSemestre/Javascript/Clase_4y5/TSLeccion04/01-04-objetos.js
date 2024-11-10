//  CLASE 4
//  VIDEO 1: Diferencias entre una variable primitiva y un objeto
let x = 10; //variable tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
//Objeto: forma basica de acceder a los objetos
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',   // VIDEO 2 CLASE 5
    nombreCompleto: function(){ // metodo o funcion en JavaScript
        return this.nombre + ' ' + this.apellido;
    },
    //  CLASE 5
    //  VIDEO 1
    get nombreEdad(){
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    },
    //  VIDEO 2
    get lang(){
        return this.idioma.toUpperCase();   // Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase(); // Convierte y guarda el cambio en idioma
    }
}

console.log(persona.nombre);

//  VIDEO 2
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);

//  VIDEO 3: agregamos metodo nombreCompleto a el objeto persona
console.log(persona.nombreCompleto());

//  VIDEO 4
console.log('Ejecutamdo con un objeto');
let persona2 = new Object();    //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salafa 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
//  VIDEO 5: otras formas de acceder a los objetos
console.log(persona["apellido"]); //Accedemos como si fuera un arreglo

//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad])
}
//  VIDEO 6
//agregar, cambiar y eliminar una propiedad a un objeto
persona.apellido = 'Betancud';  //Cambiamos dinamicamente un valor del objeto
//si se coloca mal el nombre de la prop. se creara una nueva prop
console.log(persona);

console.log('Cambiamos y eliminamos un error')
persona.apellida = 'Betancud';  //Agregamos una prop por accidente
console.log(persona)
delete persona.apellida;    //Eliminamos la prop 
console.log(persona)

//  VIDEO 7: visualizamos en el navegador el codigo

//  VIDEO 8
//Distinta formas de imprimir un objeto
//Numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distinta formas de imprimir un objeto: forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Numero 2: A traves del ciclo for in
console.log('Distinta formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Objet.values()
console.log('Distinta formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
//Convierte nuestro objeto en str (cadena)
console.log('Distinta formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

//  CLASE 5
//  VIDEO 1
console.log('Comenzamos a utilizar el metodo get:');
console.log(persona.nombreEdad); // Llamamos al get

//  VIDEO 2
console.log('Comenzamos con el metodo get para idiomas')
console.log(persona.lang) 

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

//  VIDEO 3
function Persona3(nombre = 'Luis', apelido, email){ //constructor
    this.nombre = nombre;
    this.apelido = apelido;
    this.email = email;
    //  VIDEO 4
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apelido;
    }
}
let padre = new Persona3('Leo','Lopez','lopezl@gmail.com');
padre.nombre = 'Luis';  // modificamos el nombre
padre.telefono = '5492618282821';   //Una propiedad exclusiva del objeto padre /VIDEO 6
console.log(padre);
console.log(padre.nombreCompleto()) //    VIDEO 4 / Utilizamos la funcion
let madre = new Persona3('Laura','Contrera','contreral@gmail.com');
console.log(madre.telefono) //la propiedad no esta definida /VIDEO 6
console.log(madre);

//  VIDEO 4
console.log(madre.nombreCompleto())

//  VIDEO 5
//Diferentes formas de crear objetos
//caso Objet 1
let miObjeto = new Object(); //Esta es una opcion formal
//caso Objet 2
let miObjeto2 = {}; //Esta opcion es breve y recomendada

//caso String 1
let miCadena1 = new String('Hola'); //Sintaxis formal
//caso String 2
let miCadena2 = 'hola'; //Esta es la sintaxis simplicada y recomendada

//caso con numeros 1
let miNumero = new Number(1); //Es formal no recomendable
//caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendada

//caso boolean 1
let miBoolean1 = new Boolean(false); //Formal
//caso boolean 2
let miBoolean2 = false; //Sintaxis recomendada

//caso Arreglos 1
let miArreglo1 = new Array(); //Formal
//caso Arreglos 2
let miArreglo2 = [];    //Sintaxis recomendada

//caso function 1
let miFuncion1 = new function(){};  //Todo despues de new es considerado objeto
//caso funcion 2
let miFuncion2 = function(){};  //Notacion simplificada y recomendada

//  VIDEO 6
//Uso de prototype
Persona3.prototype.telefono = '261383832'; //Agregamos una caracteristica nueva al objeto y un valor default
console.log(padre);
console.log(madre);
madre.telefono = '549261383832'
console.log(madre.telefono);

//  VIDEO 7
//Uso de call
let Persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let Persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}
console.log(Persona4.nombreCompleto2('Lic.','5492618383834'));
//call permite llamar y utilizar un metodo de un objeto en/con otro objeto que no lo tenga
console.log(Persona4.nombreCompleto2.call(Persona5, 'Ing.','5492618585856'));

//  VIDEO 8
//Metodo Apply
//a diferecia de 'call', apply no pasa los argumentos como en call
let arreglo = ['Ing.','5492618686865']; //para pasarle argumentos con apply se necesita un arreglo
console.log(Persona4.nombreCompleto2.apply(Persona5,arreglo));