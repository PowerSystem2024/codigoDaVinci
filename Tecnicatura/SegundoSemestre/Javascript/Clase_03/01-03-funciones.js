//  VIDEO 1
//Hoisting = podemos defir nuestra funcion antes o desp de llamarla
miFuncion(8, 2); //Esto es Hoisting

function miFuncion(a, b){// Una funcion puede o no tener PARAMETROS
    console.log("Sumamos: "+ (a + b));
}//Cuerpo o bloque de la funcion

//Llamando la funcion
miFuncion(5, 4);

//  VIDEO 2
function miFuncion2(a, b){
    return a + b;
}
let resultado = miFuncion2(6, 7);
console.log(resultado)

//  VIDEO 3
//Funciones de tipo expresion o funciones anonimas
let x = function(a, b){return a + b};   //  necesita cierre con punto y coma
resultado = x(5, 6);    //  al llamarla se pone la variable y parentesis
console.log(resultado);

//  VIDEO 4
//Funciones de tipo self y invoking
(function(a, b){
    console.log("Ejecutando la funcion: "+ (a+b));
})(9, 6); //esta funcion no es reutilizable

//  VIDEO 5
console.log(typeof miFuncion2);
function miFuncionDos(a, b){
    console.log(arguments.length);  //arguments solo se puede usar dentro de la funcion
}

miFuncionDos(5, 7, 3, 6);

//toString
var miFuncionTexto = miFuncionDos.toString();   //el metodo ,toString() convierte nuestra funcion a texto
console.log(miFuncionTexto);

//  VIDEO 6
//Funciones flecha                              // se la define con "const" y no con "funcion", no usa llaves,
const sumarFuncionFlecha = (a, b) => a + b;     // no necesita return, usa el operador de flecha(=>)
resultado = sumarFuncionFlecha(3, 7);   //Asignamos el valor a una variable
console.log(resultado)

//  VIDEO 7
//Parametros: son las variables que se usan al definir la funcion
//Argumentos: son las variables que se les da a las funciones cuando se la llama

//Funcion tipo expresion
let sumar = function(a = 4, b = 8){ //Esto es agregar un valor default
    console.log(arguments[0]);  //muestra el parametro de: a
    console.log(arguments[1]);   //muestra el parametro de: b    
    return a + b + (arguments[2]);
}
resultado = sumar(3, 2, 9); //js no es necesario que coninsidan la cantidad de argumentos con la cantidad de parametros
console.log(resultado);

//  VIDEO 8
//Sumar todos los argumentos y usamos hoisting
let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma;
}

// VIDEO 9
//Tipos primitivos
let k = 10;
function cambiarValor(a){   //Paso por valor
    a = 20; //Las variables dentro de una funcion no puede modificar el valor de una variable fuera de la misma
}

cambiarValor(k);
console.log(k)

//  VIDEO 10
//Paso por referencia
//Creamos un objeto
const persona = {// Buena practica definir un objeto como const
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona);

//Paso por referencia: se le pasa a la funcion o metodo le pasamos la referencia hexadecimal del espacio de memoria
function cambiarValorObjeto(p1){    //el parametro es el objeto persona, p1 guarda la direccion de memoria de el objeto utilizado
    p1.nombre = 'Ignacio';  //  parametro + . + caracteristica/atributo del objeto + = + valor del atributo nuevo + ; (esto cambia el valor en el objeto)
    p1.apellido = 'Perez';
}// luego p1 se destruye pero los cambios quedan hechos

cambiarValorObjeto(persona);
console.log(persona);