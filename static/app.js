/**
 * Define Global Variables
*/
const greeting = document.getElementById("greet");
const logOutBtn = document.getElementById("logOut");
let storedUsername = localStorage.getItem("username");

greeting.innerText = `Welcome back, ${storedUsername}`;
/**
 * End Global Variables
 * Start Helper Functions
*/

// Func: log out and clear localStorage
function logOut() {
    localStorage.clear();
};


/**
 * End Helper Functions
 * Begin Main Functions
*/

logOutBtn.addEventListener("click", logOut);
