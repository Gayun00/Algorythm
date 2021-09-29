## 🎆문제
Given the string, check if it is a palindrome.

#### Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
Input/Output

[execution time limit] 4 seconds (js)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.

## 🎆풀이
```js
function checkPalindrome(inputString) {
    const reversedString = inputString.split('').reverse().join('');
    return (inputString === reversedString) ? true : false;
}
```