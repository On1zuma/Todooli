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