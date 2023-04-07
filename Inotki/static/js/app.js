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

// Random tag color
var buttons = document.querySelectorAll('.tag-button');
var colors = ['#498ae8', '#ce99bf','#2F2FA2', '#ff698b' ,'#184bbd'];

for(var i = 0; i < buttons.length; i++) {
    buttons[i].style.backgroundColor = colors[i % colors.length];
}

// Nav link
// Get the current URL path
var currentPath = window.location.pathname;
// Get all the navbar links
var navLinks = document.querySelectorAll('.nav-link');

// Loop through each navbar link
navLinks.forEach(function(navLink) {
    // Get the href attribute of the link
    var linkHref = navLink.getAttribute('href');
    // If the href attribute matches the current URL path
    if (linkHref === currentPath) {
        // Add the 'active' class to the link
        navLink.classList.add('active');

        // Disable the link and remove cursor
        navLink.style.pointerEvents = 'none';
        navLink.style.cursor = 'none';
    }
});

var createButtonMobile = document.querySelector('.create-button-mobile');

window.addEventListener('scroll', function() {
    if (window.scrollY > 200) {
        createButtonMobile.classList.remove('hidden');
    } else {
        createButtonMobile.classList.add('hidden');
    }
});