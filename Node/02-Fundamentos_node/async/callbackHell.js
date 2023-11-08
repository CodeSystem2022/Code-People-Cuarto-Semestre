function hola(nombre, daniCallback) {
    setTimeout(function() {
        console.log('Hola '+nombre);
        daniCallback(nombre);
    }, 1000);
}

function hablar(callbackHablar){
    setTimeout(function() {
        console.log('Bla bla bla bla...');
        callbackHablar();
    }, 1000);

}

function adios(nombre, otroCallback) {
    setTimeout(function() {
        console.log('Adios '+nombre);
        otroCallback();
    }, 1500);
}
//Función recursiva
function conversacion(nombre, veces, callback) {
    if(veces > 0) {
        hablar(function() {
            conversacion(nombre, --veces, callback);
        });
    } else {
        adios(nombre, callback);
    }    
}
//--Proceso principal
console.log('Iniciando proceso...');  
hola('Carlos', function(nombre) {
    conversacion(nombre, 3, function() {
        console.log('Proceso terminado');
    });
 });
 
 //CallbackHell, no es una buena práctica. Recurrimos a una función recursiva
/*hola('Carlos', function(nombre) {
    hablar(function() {
        hablar(function() {
            hablar(function() {
                adios(nombre, function() {
                    console.log('Terminando proceso...');
                });
            });
        });
   });
});*/