function pigIt(str){
    //Code here
    /*
    split string into array
    loop through array,
    slice first letter of each word,
    concat first letter with new word and 'ay'
     */
    return str.split(' ')
    .map((word) => {
        return word.match(/[|\\/~^:,;?!&%$@*+]/) ? 
        word :`${word.slice(1)}${word[0]}ay`
    })
    .join(' ');
}

//calculations using functions

function zero(fn = null) {
    return fn ? fn(0) : 0
}

function one(fn = null) {
    return fn ? fn(1) : 1
}

function two(fn = null) {
    return fn ? fn(2) : 2
}

function three(fn = null) {
    return fn ? fn(3) : 3
}

function four(fn = null) {
    return fn ? fn(4) : 4
}

function five(fn = null) {
    return fn ? fn(5) : 5
}

function six(fn = null) {
    return fn ? fn(6) : 6
}

function seven(fn = null) {
    return fn ? fn(7) : 7
}

function eight(fn = null) {
    return fn ? fn(8) : 8
}

function nine(fn = null) {
    return fn ? fn(9) : 9
}

function plus(x) {
    return function(y) {
        return y + x;
    }
}

function minus(x) {
    return function(y) {
        return y - x;
    }
}

function times(x) {
    return function(y) {
        return y * x;
    }
}

function dividedBy(x) {
    return function(y) {
        return Math.floor(y / x);
    }
}

//create phone number
function createPhoneNumber(numbers){
    const [a, b, c, d, e, f, g, h, i, j] = numbers;
    return `(${a}${b}${c}) ${d}${e}${f}-${g}${h}${i}${j}`;
}

//Number of trailing zeros of N!

function zeros (n) {
    let counter = 0;
    /*
    num of trailing zeros in nonnegative integer
    n ! is the product of power of prime factor
    5 in n!. i.e. f(n) => {
        let sum += Math.floor((n / Math.pow(5,i)))
        while Math.pow(5,i) <= n
        i+= 1;
    }
    */
    for (let i = 1; Math.pow(5,i) <= n; i++) {
        counter += Math.floor((n / Math.pow(5,i)));
    }
    return counter;
}

console.log(zeros(9));

const romanNumerals = {
    1 : 'I', 5: 'V', 10: 'X', 50: 'L', 
    100: 'C', 500: 'D', 1000: 'M'
}

//console.log(Object.keys(romanNumerals));

/*function convertToRoman(num) {
    let romanConv = '';
    let romanKeysArr = Object.keys(romanNumerals);
    for (let i = 0; i < romanKeysArr.length; i++) {
        if (num < romanKeysArr[i]) {

            romanConv += romanKeysArr[i - 1];
            break;
        }
    }
}*/
