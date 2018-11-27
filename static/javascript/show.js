var active = 0; //Comienza en 0, es decir 0 es la primera parte
var limite_partes = 3; //Si el limite es 2 partes, la ultima parte sera la parte 1
var prefijo = "Parte_"

function select_elemento(parte){
    parte = parte.toString();
    return  document.getElementById(prefijo + parte);
}

function mostrar(parte){
    elemento = select_elemento(parte);
    elemento.classList.remove("ocultar");
}
function ocultar(parte){
    elemento = select_elemento(parte);
    elemento.classList.add("ocultar");
}
function on_off(){
    for(var i=0;i<limite_partes;i++){
        if(i==active){
            mostrar(i);
            continue;
        }
        ocultar(i)
    }
}
function next(){
    if(active+1<limite_partes){
        active+=1;
    }
    on_off();
}

function prev(){
    if(active>0){
        active-=1
    }
    on_off();
}