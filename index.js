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

//console.log(zeros(9));



//console.log(Object.keys(romanNumerals));

function convertToRoman(num) {
    const romanNumerals = {
        M: 1000, CM: 900, D: 500, CD: 400, C: 100, 
        XC: 90, L: 50, XL: 40, X: 10, IX: 9, V: 5, 
        IV: 4, I: 1,
    }
    let index = 0;
    let romanString = '';
    const romanValuesArr = Object.values(romanNumerals)
    const romanKeysArr = Object.keys(romanNumerals);
    for (let i of romanValuesArr) {
        while(num >= i) {
            //add the roman equiv of i into roman string
            index = romanValuesArr.indexOf(i);
            romanString += romanKeysArr[index];
            num -= i;
        }
    }

    return romanString;
}

function rot13(str) {
    let decodedCipher = '';
    const alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    decodedCipher = str.split('')
                       .map((letter) => {
                           let index = 0;
                           if(alphabets.includes(letter)) {
                                index = alphabets.indexOf(letter);
                                index >= 13 ? index -= 13 : index += 13;
                                return alphabets[index];
                           }
                           return letter;
                       }).join('');

    return decodedCipher;
}
  
  //console.log(rot13("SERR PBQR PNZC"));

  function high(x) {
    const alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'];

    const wordArr = x.split(' ');
    let wordClone = [];
    let sumOfLetters = 0;
    let index = 0;
    let highest = 0;
    wordArr.forEach((word) => {
        for(let letter of word) {
            if (alphabets.includes(letter)){
                index = alphabets.indexOf(letter) + 1;
                sumOfLetters += index;
            }
        }
        wordClone.push(sumOfLetters);
        sumOfLetters = 0;
    });

    for(let sumOfLetters of wordClone) {
        highest = sumOfLetters > highest ? sumOfLetters : highest;
    }
    return wordArr[wordClone.indexOf(highest)];
  }

  console.log(high('man i need a taxi up to ubud'));
  console.log(high('what time are we climbing up the volcano'));