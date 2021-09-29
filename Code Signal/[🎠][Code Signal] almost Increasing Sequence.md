## 🎆문제
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

#### Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

## 🎆풀이 - Tests passed: 17/19.
```js
function almostIncreasingSequence(sequence) {
    const arr = sequence;
    let count = 0;
    for(i = 0; i < arr.length - 1; i++) {
        if (arr[i+1] - arr[i] <= 0) {
            arr.splice(i,1);
            count++;
        }
    }
    for(i = 0; i < arr.length - 1; i++) {
    if (arr[i+1] - arr[i] <= 0) {
        arr.splice(i,1);
        count++;
    }
}
    return count === 1 ? true : false;
}
```

## 🎇다른풀이
```js
function almostIncreasingSequence(sequence) {
    var count = 0;
    for(var i=1;i<sequence.length;i++){
        if (sequence[i] <= sequence[i-1]) {
            count = count+1;
            if(count>1) {
                return false
            }
            if(sequence[i]<=sequence[i-2] && sequence[i+1]<=sequence[i-1]) {
                return false
            }
        }
    }
    return true
}
```
오름차순으로 정렬되지 않은 숫자를 발견하면 경우의 수를 나눈다.
