let sel = document.querySelectorAll(".haslo");
let hint = document.querySelector(".hint");

const canvas = document.querySelector("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const c = canvas.getContext("2d");

let koloryPink = [
    "#8a257f",
    "#943b8a",
    "#ba5bb0",
    "#8f3b85"
];

let koloryBlue = [
    "#2b6fa6",
    "#145c96",
    "#416887",
    "#456c8c"
];

let layer = [];
let layer2 = [];

function Rect(x,y,width,height,color,speed){
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.color = color;
    this.speed = speed

    this.draw = function(){
        c.beginPath();
        c.fillStyle = this.color;
        c.fillRect(this.x, this.y, this.width, this.height);
        c.fill();
    }
    this.update = function(){
        if(this.x + this.width < 0){
            this.x = canvas.width;
        }
        if(this.x > canvas.width){
            this.x = -this.width;
        }
        this.x += this.speed;
        this.draw();
    }
}

function init(){
    for(let j = 0; j < 9; j++){
        for(let i = 0; i < 40; i++){
            let randColor = Math.floor(Math.random()*koloryPink.length);
            let rect = new Rect(i*100, Math.floor(Math.random()*19)*100, 100, 100, koloryPink[randColor], 0.5);
            layer.push(rect);
        }
    }
    for(let j = 1; j < 9; j++){
        for(let i = 0; i < 40; i++){
            let randColor = Math.floor(Math.random()*koloryBlue.length);
            let rect = new Rect(i*100, Math.floor(Math.random()*19)*100, 100, 100, koloryBlue[randColor], -0.5);
            layer.push(rect);
        }
    }
}
init()

function animate(){
    c.clearRect(0,0,canvas.width, canvas.height);
    requestAnimationFrame(animate);
    for(i = 0; i < layer.length; i++){
        layer[i].update();
    }
}
animate();


sel.forEach(haslo => {
    haslo.addEventListener("focusin", ()=>{
        hint.classList.toggle("shown");
    });
    haslo.addEventListener("focusout", ()=>{
        hint.classList.toggle("shown");
    });
});

let dzien = document.querySelector(".dzien");

function createOptions(objekt, liczba){
    for(var i = 1; i <= liczba; i++){
        var opt = document.createElement("option");
        opt.value = i;
        opt.innerHTML = i;
        objekt.appendChild(opt);
    }
}

createOptions(dzien, 31);

let rok = document.querySelector(".rok");

for(var i = 2021; i >= 1950 ; i--){
    var opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    rok.appendChild(opt);
}

let miesiac = document.querySelector(".miesiac");
console.log(miesiac.length);

let selectValue;

miesiac.addEventListener("change", ()=>{
    selectValue = miesiac.options[miesiac.selectedIndex].value;
    if(selectValue == "01" || selectValue == "03" || selectValue == "05" || selectValue == "07" || selectValue == "08" || selectValue == "10" || selectValue == "12"){
        while(dzien.firstChild){
            dzien.removeChild(dzien.firstChild);
        }
        createOptions(dzien, 31);
    }else if(selectValue == "02"){
        while(dzien.firstChild){
            dzien.removeChild(dzien.firstChild);
        }
        createOptions(dzien, 29);
    }else{
        while(dzien.firstChild){
            dzien.removeChild(dzien.firstChild);
        }
        createOptions(dzien, 30);
    }
});

let error = document.querySelector(".error");

if(typeof(error) != undefined && error != null){
    setTimeout(()=>{
        error.style.transform = "translateY(-300px)";
    }, 5000);
}


/*Animacja tła */

