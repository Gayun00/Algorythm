## ๐๋ฌธ์ 
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

#### Example

For `n = 1230`, the output should be
`isLucky(n) = true`;
For `n = 239017`, the output should be
`isLucky(n) = false`.

## ๐ํ์ด
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

## โจ๋ค๋ฅธ ํ์ด
```js
function isLucky(n) {
    var count = 0;
    n = String(n).split('').map(t => {return parseInt(t)});
    n.forEach( (el, i) => { (i < n.length / 2) ? count += el : count -= el });
    return count == 0;
}
```

๋๋ ์ map์ผ๋ก ์ซ์ํ์ผ๋ก ๋ณํํ๋๊ฒ ์๋์๊น?
return๋ฌธ์ ์ ๋๋ก ์ฐ์ง ์์์์์๊น?
์ฐ๋ฉด์๋ ๊ต์ฅํ ๋นํจ์จ์ ์ด๊ณ  ๋ฒ๊ฑฐ๋ก์ด ์ฝ๋๋ผ๊ณ  ๋๊ผ๊ธฐ ๋๋ฌธ์, ๊ผญ ๋ค๋ฅธ ํ์ด๋ฅผ ์ฐธ๊ณ ํด ๋ฏ์ด๋ณด๊ณ  ๊ณต๋ถํ์.