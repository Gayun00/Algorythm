## 🎆 Description
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

#### Example

For `inputArray = [1, 2, 1]`, `elemToReplace = 1`, and `substitutionElem = 3`, the output should be
`arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3]`.

<br>
<br>

## 🎇 Solution
```js
function arrayReplace(inputArray, elemToReplace, substitutionElem) {
    const arr = [...inputArray];
    let indexArr = [];
    let index = arr.indexOf(elemToReplace);
    
    while(index !== -1) {
        indexArr.push(index);
        index = arr.indexOf(elemToReplace, index + 1);
    }
    indexArr.forEach((idx) => {
        arr.splice(idx, 1, substitutionElem)
    })    
    return arr;
}
```

<br>
<br>

## 🎁 Review
>이 알고리즘을 풀면서 사용한 메소드에 대해 정리해 놓았다.
[배열 안 모든 요소의 항목 찾기 - 오늘자 포스트](https://velog.io/@gygy/%EB%B0%B0%EC%97%B4%EC%95%88-%EA%B0%99%EC%9D%80-%EC%9A%94%EC%86%8C%EC%9D%98-%EB%AA%A8%EB%93%A0-%EC%9C%84%EC%B9%98-%EC%B0%BE%EA%B8%B0indexOf-2nd-param)
