//nav box shadow
window.addEventListener('scroll',(e)=>{
  const nav = document.querySelector('.nav');
  if(window.pageYOffset>0){
    nav.classList.add("add-shadow");
  }else{
    nav.classList.remove("add-shadow");
  }
});

//burger
let toggle = document.querySelector('.toggle');
let body = document.querySelector('body');

toggle.addEventListener('click', function () {
  body.classList.toggle('open');
})

//flash message
const button = document.querySelector("button"),
    toast = document.querySelector(".toast");
if(toast){
  (closeIcon = document.querySelector(".close")),
      (progress = document.querySelector(".progress"));

  let timer1, timer2;

  if (document.getElementsByClassName('alert')) {
    toast.classList.add("active");
    progress.classList.add("active");

    timer1 = setTimeout(() => {
      toast.classList.remove("active");
    }, 5000); //1s = 1000 milliseconds

    timer2 = setTimeout(() => {
      progress.classList.remove("active");
    }, 5300);
  };

  closeIcon.addEventListener("click", () => {
    toast.classList.remove("active");

    setTimeout(() => {
      progress.classList.remove("active");
    }, 300);

    clearTimeout(timer1);
    clearTimeout(timer2);
  });
}

document.addEventListener("DOMContentLoaded", function(event) {
    var scrollpos = sessionStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo({
        top: scrollpos,
        behavior: 'instant'
    });
});

window.onbeforeunload = function(e) {
    sessionStorage.setItem('scrollpos', window.scrollY);
};

window.onpopstate = function(e) {
    var scrollpos = sessionStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo({
        top: scrollpos,
        behavior: 'instant'
    });
};

// random tag color
var buttons = document.querySelectorAll('.tag-button');
var colors = ['#498ae8', '#ce99bf','#2F2FA2', '#ff698b' ,'#184bbd'];

for(var i = 0; i < buttons.length; i++) {
    buttons[i].style.backgroundColor = colors[i % colors.length];
}