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

//go back to the same position on reload
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


//home effect
const text1 = "Inolii <i class='fa-solid fa-feather-pointed'></i>, Revolutionize Your Management, <br>";
const text2 = "Achieve your goals! <i class='fa-solid fa-dove'></i>";

// Get the <p> and <strong> elements
const p = document.getElementById("live-text1");
const strong = document.getElementById("live-text2");

// Get <i> tags
const itag1 = p.getElementsByTagName('i')[0];
const itag2 = strong.getElementsByTagName('i')[0];

// Create an empty string to store the typed text for <p>
let typedText1 = "";

// Create an empty string to store the typed text for <strong>
let typedText2 = "";

// Create a variable to keep track of the current index in the text for <p>
let index1 = 0;

// Create a variable to keep track of the current index in the text for <strong>
let index2 = 0;

// Clear the innerHTML of <p> and <strong>
p.innerHTML = "";
strong.innerHTML = "";

// Create a function to simulate typing for <p>
function type1() {
    // If the current index is less than the length of the text
    if (index1 < text1.length) {
        // Add the current character to the typedText string
        typedText1 += text1[index1];
        // Update the <p> element's innerHTML to match the typedText
        p.innerHTML = typedText1;
        // Increment the index
        index1++;
        // Use setTimeout to call the type function after a certain amount of time
        setTimeout(type1, 30);
        if(index1 === text1.length){
            itag1.classList.add("fa-solid", "fa-feather-pointed");
        }
    }
}

// Create a function to simulate typing for <strong>
function type2() {
    // If the current index is less than the length of the text
    if (index2 < text2.length) {
        // Add the current character to the typedText string
        typedText2 += text2[index2];
        // Update the <strong> element's innerHTML to match the typedText
        strong.innerHTML = typedText2;
        // Increment the index
        index2++;
        // Use setTimeout to call the type function after a certain amount of time
        setTimeout(type2, 30);
        if(index2 === text2.length){
            itag2.classList.add("fa-solid", "fa-dove");
        }
    }
}

// Clear the innerHTML of <p> and <strong>
p.innerHTML = "";
strong.innerHTML = "";

// Call the type1() function to start the animation for <p>
type1();

// Call the type2() function to start the animation for <strong> after a certain time
setTimeout(type2, 3500);