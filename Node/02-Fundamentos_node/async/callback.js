/*function soyAsincrona(daniCallback) {
    setTimeout(function() {
        console.log('Hola, soy una función asíncrona');
        daniCallback();
    }, 1000);
}
console.log('Iniciando proceso...');   
soyAsincrona(function() {
    console.log('Terminando proceso...');
});*/   
//Comentamos el código anterior ya que haremos algunos 
//cambios en el código para hacerlo más complejo, pero
//la idea es que quede lo hecho también.

function hola(nombre, daniCallback) {
    setTimeout(function() {
        console.log('Hola '+nombre);
        daniCallback(nombre);
    }, 1000);
}

function adios(nombre, otroCallback) {
    setTimeout(function() {
        console.log('Adios '+nombre);
        otroCallback();
    }, 1000);
}

/*console.log('Iniciando proceso...');   
hola('Carlos', function() {
    adios('Carlos', function() {
        console.log('Terminando proceso...');
    });//LLamamos una función dentro de otra 
});*/

//hola('Carlos', function() {});
//adios('Carlos', function() {});
//Utilizando variables compartidas (ej, Carlos)

console.log('Iniciando proceso...');   
hola('Carlos', function(nombre) {
    adios(nombre, function() {
        console.log('Terminando proceso...');
    });
});