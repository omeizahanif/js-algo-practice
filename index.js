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


console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));
console.log(createPhoneNumber([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]));