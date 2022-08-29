// program to print prime numbers between the two numbers

// take input from the user
var lowerNumber = parseInt(window.prompt('Enter lower number: '));
var higherNumber = parseInt(window.prompt('Enter higher number: '));

console.log("The prime numbers between ${lowerNumber} and ${higherNumber} are:");

// looping from lowerNumber to higherNumber
for (var i = lowerNumber; i <= higherNumber; i++) {
    var flag = 0;

    // looping through 2 to user input number
    for (var j = 2; j < i; j++) {
        if (i % j == 0) {
            flag = 1;
            break;
        }
    }

    // if number greater than 1 and not divisible by other numbers
    if (i > 1 && flag == 0) {
        console.log(i);
    }
}