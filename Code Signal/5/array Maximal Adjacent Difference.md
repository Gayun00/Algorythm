## 🎆문제
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

#### Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.

## 🎇풀이
```js
function arrayMaximalAdjacentDifference(inputArray) {
    let result = [];
    for(i = 0; i < inputArray.length-1; i++) {
        let arr = [inputArray[i],inputArray[i+1]]
        result.push(Math.max(...arr)-Math.min(...arr))
    }
    return Math.max(...result)
}
```