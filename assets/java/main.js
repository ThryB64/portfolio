const menu=() => {
    const menu2 = document.querySelector('.menu2');
    const menu1 = document.querySelector('.menu');
    const ligne1 = document.querySelector('.ligne1');
    const ligne2 = document.querySelector('.ligne2');
    const ligne3 = document.querySelector('.ligne3');
    const btn = document.querySelector(".button");
    const back = document.querySelector(".accueil video");
    const vid = document.querySelector(".video");
    const vid2 = document.querySelector(".video2");
    const btn2 = document.querySelector(".button2");
    
    const popups = document.querySelector(".popups");
    const cross = document.querySelector(".cross");

    const items1 = document.querySelector(".items1");
    const pop1 = document.querySelector(".pop1");

    const items2 = document.querySelector(".items2");
    const pop2 = document.querySelector(".pop2");

    const items3 = document.querySelector(".items3");
    const pop3 = document.querySelector(".pop3");

    const items4 = document.querySelector(".items4");
    const pop4 = document.querySelector(".pop4");

    const items5 = document.querySelector(".items5");
    const pop5 = document.querySelector(".pop5");

    const items6 = document.querySelector(".items6");
    const pop6 = document.querySelector(".pop6");

    menu2.addEventListener('click',()=>{
        menu1.classList.toggle('menu2-anim')
        ligne1.classList.toggle('ligne1-anim')
        ligne2.classList.toggle('ligne2-anim')
        ligne3.classList.toggle('ligne3-anim')

    });
    back.addEventListener('click',()=>{
        btn2.classList.toggle('button2-anim') 
        btn.classList.toggle('button-anim')
        vid2.classList.toggle('video2-anim')
        vid.classList.toggle('video-anim')
    });
    cross.addEventListener('click',()=>{
        popups.classList.remove("popups-activate")
        pop1.classList.remove("pop1-activate")
        pop2.classList.remove("pop2-activate")
        pop3.classList.remove("pop3-activate")
        pop4.classList.remove("pop4-activate")
        pop5.classList.remove("pop5-activate")
        pop6.classList.remove("pop6-activate")
    });
    items1.addEventListener('click',()=>{
        popups.classList.toggle("popups-activate")
        pop1.classList.toggle('pop1-activate')
    });
    items2.addEventListener('click',()=>{
        popups.classList.toggle("popups-activate")
        pop2.classList.toggle('pop2-activate')
    });
    items3.addEventListener('click',()=>{
        popups.classList.toggle("popups-activate")
        pop3.classList.toggle('pop3-activate')
    });
    items4.addEventListener('click',()=>{
        popups.classList.toggle("popups-activate")
        pop4.classList.toggle('pop4-activate')
    });
    items5.addEventListener('click',()=>{
        popups.classList.toggle("popups-activate")
        pop5.classList.toggle('pop5-activate')
    });
    items6.addEventListener('click',()=>{
        popups.classList.toggle("popups-activate")
        pop6.classList.toggle('pop6-activate')
    });
}
window.onload=function(){
    menu();
}




