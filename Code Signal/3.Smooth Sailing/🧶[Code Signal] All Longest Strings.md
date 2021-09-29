## 🎆문제
Given an array of strings, return another array containing all of its longest strings.

Example

For `inputArray = ["aba", "aa", "ad", "vcd", "aba"]`, the output should be
`allLongestStrings(inputArray) = ["aba", "vcd", "aba"]`.

## 🎇풀이
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

## ✨다른 풀이
```js
function allLongestStrings(inputArray) {
    'use strict';
    let maxSize = Math.max(...inputArray.map(x => x.length));
    return inputArray.filter(x => x.length === maxSize);
}
```
아아... 늘 map과 filter를 사용하는 데 익숙하지 않다.
여기서는 inputArray의 요소들을 순회하며 길이를 바로 배열로 만들었다.
그 다음 최대 길이와 길이가 동일한 배열만 필터링 해주었다.
훨씬 간결한 코드를 작성할 수 있으니, map과 filter를 이요해서 꼭 한 번 다시 풀어봤으면 한다.
