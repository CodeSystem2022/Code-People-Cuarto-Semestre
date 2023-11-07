//global === this = true

//Mostrar algo en consola
/*console.log();

//Mostrar un mensaje de error  
console.error();

//Ejecutar un código después de un tiempo   
setTimeout(() => {}, 1000);

//Ejecutar un código cada cierto tiempo
setInterval(() => {}, 1000);    

setImmediate(() => {}); //Se ejecuta inmediatamente*/

//console.log(setInterval);

/*let i = 0;
let intervalo = setInterval(() => {
    console.log('Hola');
    if (i === 3) {
        clearInterval(intervalo);//detenemos la función
    }
    i++;
}, 1000);*/

setImmediate(() => {
    console.log('Saludo inmediato');
});

//require(); //requerir módulos

//console.log(process); //Información del proceso actual

//console.log(__dirname); //Directorio actual
//console.log(__filename); //Nombre del archivo actual

global.miVariable = 'mi variable global';
console.log(miVariable);