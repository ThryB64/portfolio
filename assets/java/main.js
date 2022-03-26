

const menu=() => {
    const menu2 = document.querySelector('.menu2');
    const menu1 = document.querySelector('.menu');
    menu2.addEventListener('click',()=>{
        menu1.classList.toggle('menu2-anim')
    });
}
window.onload=function(){
    menu();
    scroll();
}
const scroll=() => {
    window.addEventListener('scroll',()=>{
        console.log('bonjour')
    });
}

