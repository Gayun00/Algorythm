## 🎆문제
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

#### Example

For `n = 1230`, the output should be
`isLucky(n) = true`;
For `n = 239017`, the output should be
`isLucky(n) = false`.

## 🎇풀이
```js
function isLucky(n) {
    const strArr = String(n).split('');
    const firstArr = strArr.slice(0,strArr.length/2);
    const secondArr = strArr.slice(strArr.length/2);

    for(i=0; i<firstArr.length; i++) {
        firstArr[i] = Number.parseInt(firstArr[i])
    }
    for(i=0; i<secondArr.length; i++) {
        secondArr[i] = Number.parseInt(secondArr[i])
    }
    const sumFirstArr = firstArr.reduce((sum, curr) => {
        return sum + curr;
    })
    const sumSecondArr = secondArr.reduce((sum, curr) => {
        return sum + curr;
    })

    return sumFirstArr === sumSecondArr;
}
```

## ✨다른 풀이
```js
function isLucky(n) {
    var count = 0;
    n = String(n).split('').map(t => {return parseInt(t)});
    n.forEach( (el, i) => { (i < n.length / 2) ? count += el : count -= el });
    return count == 0;
}
```

나는 왜 map으로 숫자형으로 변형하는게 안됐을까?
return문을 제대로 쓰지 않아서였을까?
쓰면서도 굉장히 비효율적이고 번거로운 코드라고 느꼈기 때문에, 꼭 다른 풀이를 참고해 뜯어보고 공부하자.