## 🎆문제
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

#### Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

## 🎇풀이
```js
function addBorder(picture) {
    let original = picture;
    const starCount = original[0].length + 2;
    const star = "*";
    let matrix = new Array(starCount).fill(star).join('');

    original = original.map((str) => {return star + str + star})
    original.splice(0, 0, matrix)
    original.splice(original.length, 0, matrix)

    return original;
}

```
## ✨다른 풀이
```js
function addBorder(picture) {
    var width = picture[0].length + 2;
    return [
        '*'.repeat(width),
        ...picture.map(line => `*${line}*`),
        '*'.repeat(width)
    ];
}

```
아...맞다. repeat을 쓰면 문자열로 반복이 가능했는데 잊어버렸다.
그리고 배열에 직접 써주어 바로 리턴해 코드가 훨씬 간결해졌다.
