## 🎆문제
Given two strings, find the number of common characters between them.

Example

For `s1 = "aabcc"` and `s2 = "adcaa"`, the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

## 🎇풀이
```js
function commonCharacterCount(s1, s2) {
    const s1arr = s1.split('');
    const s2arr = s2.split('');
    let count = 0;
    for(i = 0; i < s1arr.length; i++) {
        if(s2arr.includes(s1arr[i])) {
            count++;
            s2arr.splice(s2arr.indexOf(s1arr[i]), 1)
        }
    }
    return count;
}
```

## ✨다른 풀이
```js
function commonCharacterCount(s1, s2) {
    for (var i = 0; i < s1.length; i++) {
        s2 = s2.replace(s1[i], "!");
    }
    return s2.replace(/[^!]/g, "").length;
}
```
정규표현식을 사용했다.
