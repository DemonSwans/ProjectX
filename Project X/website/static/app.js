
let btn = document.querySelector(".btn");
let swt = document.querySelector(".switch");
let hl = document.querySelectorAll(".hiperlink");
    
btn.addEventListener("click", ()=>{
    btn.classList.toggle("switched");
    document.body.classList.toggle("bg");
    hl.style.color = "black";
});