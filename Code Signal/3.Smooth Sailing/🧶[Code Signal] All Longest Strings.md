## ๐๋ฌธ์ 
Given an array of strings, return another array containing all of its longest strings.

Example

For `inputArray = ["aba", "aa", "ad", "vcd", "aba"]`, the output should be
`allLongestStrings(inputArray) = ["aba", "vcd", "aba"]`.

## ๐ํ์ด
```js
function allLongestStrings(inputArray) {
    let arrLength = [];
    let result = [];
    inputArray.forEach((str) => {arrLength.push(str.length)});
    const maxLength = Math.max(...arrLength);
    inputArray.forEach((str) => {
        if(str.length === maxLength) {
            result.push(str);
        }
    })
    return result;
}
```

## โจ๋ค๋ฅธ ํ์ด
```js
function allLongestStrings(inputArray) {
    'use strict';
    let maxSize = Math.max(...inputArray.map(x => x.length));
    return inputArray.filter(x => x.length === maxSize);
}
```
์์... ๋ map๊ณผ filter๋ฅผ ์ฌ์ฉํ๋ ๋ฐ ์ต์ํ์ง ์๋ค.
์ฌ๊ธฐ์๋ inputArray์ ์์๋ค์ ์ํํ๋ฉฐ ๊ธธ์ด๋ฅผ ๋ฐ๋ก ๋ฐฐ์ด๋ก ๋ง๋ค์๋ค.
๊ทธ ๋ค์ ์ต๋ ๊ธธ์ด์ ๊ธธ์ด๊ฐ ๋์ผํ ๋ฐฐ์ด๋ง ํํฐ๋ง ํด์ฃผ์๋ค.
ํจ์ฌ ๊ฐ๊ฒฐํ ์ฝ๋๋ฅผ ์์ฑํ  ์ ์์ผ๋, map๊ณผ filter๋ฅผ ์ด์ํด์ ๊ผญ ํ ๋ฒ ๋ค์ ํ์ด๋ดค์ผ๋ฉด ํ๋ค.
