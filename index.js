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


console.log(pigIt('Pig latin is cool'));
console.log(pigIt('Hello world !'));