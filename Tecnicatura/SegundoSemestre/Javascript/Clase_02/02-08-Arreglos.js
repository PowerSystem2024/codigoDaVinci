//Clase 2 JAVASCRIPT
//CREACION DE ARRAY O ARREGLOS
//let autos = new Array('Ferrari', 'Renault', 'BMW')  Esta es una forma vieja de declararlos
const autos = ['Ferrari', 'Renault', 'BMW'] //la referencia de memoria es CONST
console.log(autos);

//Recorremos los elementos de un arreglo (V2)
console.log(autos[0]); //De esta forma se accede al primer eleto
console.log(autos[2]);

//al poner el punto luego de autos, podemos acceder a varias funciones o metodos incorporados para arrays
for(let i = 0; i < autos.length; i++){
console.log(i+':'+autos[i]);
}

//Modificamos los elementos del arreglo (V3)
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi'); //esta funcion lo agrega al final
console.log(autos);

autos[autos.length] = 'Porche';
//Otras formas de agregar elementos al arreglo
console.log(autos);

// Tercera forma de agregar elementos al arreglo. En esta forma hay que tener mas cuidado y detalle
autos[6] = 'Renault';
console.log(autos); //Este espacio ocupa memoria

//Como preguntamos si es un Array o Arreglo (V4)
console.log(Array.isArray(autos)); //Devuelve un booleano

console.log(autos instanceof Array); //Preguntamos si la variables es una instaceof clase array