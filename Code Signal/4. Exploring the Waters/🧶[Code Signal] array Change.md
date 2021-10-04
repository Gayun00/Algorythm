## 🎆문제
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

#### Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

## 🎇풀이
```js
function arrayChange(inputArray) {
    let increaseCount = 0;
    let totalCount = 0;

    for(i = 0; i < inputArray.length; i++) {
        if (inputArray[i+1] - inputArray[i] < 1) {
            increaseCount = (inputArray[i] - inputArray[i+1] + 1);
            totalCount += increaseCount;
            inputArray[i+1] += increaseCount;
        }
    }
    return totalCount;
}
```

## ✨다른 풀이
```js
function arrayChange(inputArray) {
    return inputArray.reduce(function(x,b,i,a){
        while(b >= a[i+1]){x++; a[i+1]++;};
        return x;
    },0)
}
```
- reduce를 사용해 풀었는데, 언뜻 봐서는 이해가 잘 되지 않는다. 하나하나 따져보자.

## ✨다른 풀이 2
```js
function arrayChange(series) {
    var moves = 0;

    for (var i = 1; i < series.length; i++) {
        if (series[i] <= series[i - 1]) {
            diff = series[i - 1] - series[i] + 1;
            series[i] += diff;
            moves += diff;
        }
    }

    return moves;
}
```
- diff는 따로 변수 지정하지 않아도 쓸 수 있는 건가? 풀이 방식은 나와 똑같은데, 변수 지정을 보다 간결하게 했다.

