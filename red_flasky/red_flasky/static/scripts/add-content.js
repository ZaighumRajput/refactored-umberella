/*
The is a multiline comment
*/
var today   = new Date();
var hourNow = today.getHours();
var greeting;

//Display the appropriate greeting based on the current time
if (hourNow > 18) {
    greeting = 'Good Evening!';
}
else if (hourNow > 12) {
    greeting = 'Good afternoon!';
}
else if (hourNow > 0) {
    greeting = 'Good morning!';
}
else
{
    greeting = 'Welcome!';
}//coding blocks don't end with a semi-colon

document.write('<h3>' + greeting + '</h3>' )