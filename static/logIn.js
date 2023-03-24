/**
 * Define Global Variables
*/
const greeting = document.getElementById("greet");
const textBox = document.getElementById("textBox");
const logInBtn = document.getElementById("logIn");
const errorMSG = document.getElementById("errorMSG");
let storedUsername = localStorage.getItem("username");


/**
 * End Global Variables
 * Start Helper Functions
*/
// Func: log in and store localStorage
function logIn() {
    let userName = textBox.value;
    if (userName.trim() != "") {
        localStorage.setItem("username", userName.trim());
        window.location.href = "/";
    } else {
        errorMSG.innerText = "Empty Field!"
    }
}

/**
 * End Helper Functions
 * Begin Main Functions
*/

logInBtn.addEventListener("click", logIn);