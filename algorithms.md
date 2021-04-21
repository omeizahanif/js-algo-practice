## 1 Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pigIt('Pig latin is cool !'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !

## 2 Calculating with Functions
we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

## 3 create phone number 
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

## 4 Number of trailing zeros of N!

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

## 5 Roman Numeral Converter

Convert the given number into a roman numeral.
All roman numerals answers should be provided in upper-case.
Example: 

convertToRoman(2) should return the string 'II'
convertToRoman(3999) should return the string 'MMMCMXCIX'

## 6 Caesars Cipher

Write a function which takes a ROT13 encoded string as input and returns a decoded string.

All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), but do pass them on.
Example: rot13("SERR PBQR PNZC") should decode to the string FREE CODE CAMP

## 7 Highest Scoring Word

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
Example: high('what time are we climbing up the volcano') should return volcano