
//home effect
const text1 = "Igonii <i class='fa-solid fa-feather-pointed'></i>, Revolutionize Your Management,";
const text2 = "Achieve your goals! <i class='fa-solid fa-dove'></i>";

// Get the <p> and <strong> elements
const p = document.getElementById("live-text1");
const strong = document.getElementById("live-text2");

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
    }
}

// Clear the innerHTML of <p> and <strong>
p.innerHTML = "";
strong.innerHTML = "";

// Call the type1() function to start the animation for <p>
type1();

// Call the type2() function to start the animation for <strong> after a certain time
setTimeout(type2, 3500);