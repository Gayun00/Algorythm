## πλ¬Έμ 
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

#### Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

## πνμ΄
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

## β¨λ€λ₯Έ νμ΄
```js
function arrayChange(inputArray) {
    return inputArray.reduce(function(x,b,i,a){
        while(b >= a[i+1]){x++; a[i+1]++;};
        return x;
    },0)
}
```
- reduceλ₯Ό μ¬μ©ν΄ νμλλ°, μΈλ» λ΄μλ μ΄ν΄κ° μ λμ§ μλλ€. νλνλ λ°μ Έλ³΄μ.

## β¨λ€λ₯Έ νμ΄ 2
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
- diffλ λ°λ‘ λ³μ μ§μ νμ§ μμλ μΈ μ μλ κ±΄κ°? νμ΄ λ°©μμ λμ λκ°μλ°, λ³μ μ§μ μ λ³΄λ€ κ°κ²°νκ² νλ€.

