/*Promesas
Es una sintaxis más elegante, legible, y escalable que un callback.
Tiene 3 estados: resolve, reject, pending
Son una clase global que podemos llamar de donde sea
Son útiles para visualizar código asíncrono de forma síncrona
Es una función que recibe dos parámetros: resolve (retorna el valor deseado) 
y reject (valor no deseado, hasta un error puede ser)
Usamos la propiedad .then() para ejecutar la promesa 
y .catch() para capturar el error
*/

function hola(nombre) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log('Hola '+nombre);
            resolve(nombre);
        }, 1000);
    });
}

function hablar(nombre){
    return new Promise((resolve, reject) => {
        setTimeout(function() {
            console.log('Bla bla bla bla...');
            resolve(nombre);
        }, 1000);
    });
}

function adios(nombre) {
    return new Promise((resolve, reject) => {
        setTimeout(function() {
            console.log('Adios '+nombre);
            //resolve();
            reject('Hay un error');
        }, 1000);
    });
}
//Llamamos a la función
console.log('Iniciando proceso...');
hola('Carlos')
    .then(hablar)
    .then(hablar)
    .then(hablar)
    .then(adios)
    .then((nombre) => {
        console.log('Terminando proceso...');
    })
//Capturamos el error (siempre que usemos promesas, es necesario capturar el error))      
    .catch(error => {
        console.error('Ha habido un error:');
        console.error(error);
    })