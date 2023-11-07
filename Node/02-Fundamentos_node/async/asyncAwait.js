//La palabra async no es necesaria en las funciones porque ya son asíncronas
//igual proyectan una sincronía visual
async function hola(nombre) {//ponemos la marca de async para indicar que es una función asíncrona
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            console.log('Hola '+nombre);
            resolve(nombre);
        }, 1000);
    });
}

async function hablar(nombre){
    return new Promise((resolve, reject) => {
        setTimeout(function() {
            console.log('Bla bla bla bla...');
            resolve(nombre);
        }, 1000);
    });
}

async function adios(nombre) {
    return new Promise((resolve, reject) => {
        setTimeout(function() {
            console.log('Adios '+nombre);
            resolve();
            //reject('Hay un error');
        }, 1000);
    });
}

//await hola('Carlos'); esto es una sintaxis incorrecta
//await sólo es válido dentro de una función asíncrona

async function main() {
    let nombre = await hola('Carlos');
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre);
    console.log('Terminamos el proceso');

}
console.log('Empezamos el proceso');
main();

//Falta pasar el código a inglés