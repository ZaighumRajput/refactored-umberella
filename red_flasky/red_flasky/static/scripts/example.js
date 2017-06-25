// Create variables for the welcome message
var greeting = 'Howdy';
var name     = 'Molly';
var message  = ' , please check your order';

// Concactenate the three variables above to create the welcome message
var welcome = greeting + name + message;

// Create variables to hold details about sign
var sign       = 'Montague House';
var tiles     = sign.length;
var subTotal   = tiles * 5;
var shipping   = 7;
var grandTotal = subTotal + shipping;

//Get the element that has an id of greeting
var el = document.getElementById('greeting');
// Replace the content
el.textContent = welcome;

var elSign = document.getElementById('userSign');
elSign.textContent = sign;

var elTiles = document.getElementById('tiles');
elTiles.textContent = tiles;

var elSubTotal = document.getElementById('subTotal');
elSubTotal.textContent = '$' + subTotal;

var elShipping = document.getElementById('shipping');
elShipping.textContent = '$' + shipping;

var elGrandTotal = document.getElementById('grandTotal');
elGrandTotal.textContent = '$' + grandTotal;
