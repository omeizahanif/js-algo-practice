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
    wordArr.forEach((word) => {
        for(let letter of word) {
                sumOfLetters += alphabets.indexOf(letter);
        }
        wordClone.push(sumOfLetters);
        sumOfLetters = 0;
    });

    return wordArr[wordClone.indexOf(Math.max(...wordClone))];
  }

// TODO: complete this object/class

// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
function PaginationHelper(collection, itemsPerPage){
  this.collection = collection;
  this.itemsPerPage = itemsPerPage;
}

// returns the number of items within the entire collection
PaginationHelper.prototype.itemCount = function() {

    return this.collection.length;
}

// returns the number of pages
PaginationHelper.prototype.pageCount = function() {

    return Math.ceil(this.collection.length / this.itemsPerPage);
}

// returns the number of items on the current page. page_index is zero based.
// this method should return -1 for pageIndex values that are out of range
PaginationHelper.prototype.pageItemCount = function(pageIndex) {
    const pageArray = [];
    const collection = this.collection;
    if (this.pageCount() > pageIndex) {
        for (let i = 0; i <= pageIndex; i++) {
            pageArray.push(collection.splice(0,this.itemsPerPage));    
        }
        return pageArray[pageIndex].length;
    }

    return -1;
    
}

// determines what page an item is on. Zero based indexes
// this method should return -1 for itemIndex values that are out of range
PaginationHelper.prototype.pageIndex = function(itemIndex) {
    const collection = this.collection;
    const item = collection[itemIndex];
    const pageArray = [], pageCount = this.pageCount();
    let index = 0;

    //if (collection.length == 0 && ) return 0; 

    if (collection.length > itemIndex && itemIndex >= 0) {
        for (let i = 0; i < pageCount; i++) {
            pageArray.push(collection.splice(0,this.itemsPerPage));    
        }
    
        for (let page of pageArray) {
            page.includes(item) ? index = pageArray.indexOf(page) : -1 
        }


        return index;
    }
    
    return -1;

}

//let helper = new PaginationHelper([21, 22, 23, 24], 10);

function solution(list){
    let clone = [...list], rangeArr = [],
    mainStr = '', i = 0, fixedLength = clone.length;
    while (i < fixedLength) {
        //evaluate diff btw 2nd and 1st value
        if((clone[1] - clone[0]) === 1) {
            //shift 1st value into an rangeArr
            rangeArr.push(clone.shift());
        } else {
            rangeArr.push(clone.shift());
            //concat the result of calling format on rangeArr
            mainStr += format(rangeArr);
            //reset rangeArr to be used in next iteration
            rangeArr = [];
        }      
        i += 1;
    }

    /**
     * format takes an array, and, based on num of values,
     * transforms it into a string containing either a 
     * range of values, or concatenated single unrelated values
     * @param {an array with arbitrary num of values} arr 
     * @returns {a string formatted based on num of values}
     */
    function format(arr) {
        if(arr.length >= 3) {
            return `${arr[0]}-${arr[arr.length - 1]},`
        } else {
            return arr.reduce((acc, curr) => `${acc}${curr},`, '');
        }
    }
    //return main str, removing the last delimiter (,)
    return mainStr.substring(0, mainStr.length-1);
}

console.log(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
