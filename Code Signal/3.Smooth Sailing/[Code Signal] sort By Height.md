## ๐๋ฌธ์ 
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

#### Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

## ๐ํ์ด - Hidden Test 1๊ฐ ์คํจ

```js
function sortByHeight(a) {
    if(a.every((el) => {return el === -1})){return a}

    let peopleOnly = [];
    peopleOnly = a.filter((el) => {
        return el !== -1
    })

    const sorted = peopleOnly.sort((a,b) => {return a - b});
    for(i = 0; i < sorted.length; i++) {
        if(a[i] === -1) {
            sorted.splice(i,0,-1)
        }
    }
    return sorted;
}
```
Hidden Test ํ ๋ฌธํญ์ ํต๊ณผํ์ง ๋ชปํ๋ค.. ์ด๋ค ๊ฒ ๋๋ฌธ์ผ๊น?

## โจ๋ค๋ฅธ ํ์ด
```js
function sortByHeight(a) {
    let aFiltered = a.filter(x => {
        if(x !== -1 ){
            return x;
        }
    }).sort((a,b) => a-b);

    for(let i = 0; i < a.length; i++) {
        if(a[i] != -1) {
            a[i] = aFiltered.shift();
            console.log(a[i],aFiltered)
        }
    }

    return a;
}
//https://gist.github.com/RahmatSaeedi/be4d23110624e526e95958c8067cb9d6
```
- ์ฌ๊ธฐ์์  shift()๋ฉ์๋๋ฅผ ์ฌ์ฉํ๋ค.
aFiltered์๋ -1์ ์ ์ธํ ์ฌ๋์ ํค๋ง ๋ฃ์ด๋์๋๋ฐ, aFiltered.shift()๋ ์ฒซ๋ฒ์งธ ์์ ํ๋๋ฅผ ๋ฐฐ์ด์์ ์ ๊ฑฐ ํ ํ ์ด ์์๋ฅผ ๋ฐํํ๋ค. ์๋ณธ ๋ฐฐ์ด ์ค -1์ด ์๋ ์์๋ฅผ ์ ๊ฑฐ ํ ๋ค ๋ฐํ๋ aFiltered์ ์ฒซ๋ฒ์งธ ์์๋ก ๋์ฒดํ๋ ๊ฒ์ ๋ฐ๋ณตํ๋ค.
์ฆ, aFiltered์ ์ฒซ๋ฒ์งธ ์์๋ ๊ณ์ ์ ๊ฑฐ ๋๋ for๋ฌธ์ด ๋ ๋๋ง๋ค ์ฐจ๋ก๋๋ก ๋ชจ๋  ์์๋ฅผ ๊ฑฐ์น๋ฏ๋ก, ์ ๋ ฌ๋ ๋ฐฐ์ด์ ์์๋ค๋ก ์์ฐจ์ ์ผ๋ก ์๋ณธ ๋ฐฐ์ด์ -1์ด ์๋ ์์๋ค์ ๋์ฒด์ํจ๋ค.

### ๋ค์ ํ์ด๋ณด์๋ค. ํด๊ฒฐ!
```js
function sortByHeight(a) {

    if(a.every((el) => {return el === -1})){return a}

    let peopleOnly = [];
    peopleOnly = a.filter((el) => {
        return el !== -1
    }).sort((a,b) => {return a - b});
    //๊ตณ์ด ํ์์๋ sorted ๋ณ์ ์ง์  ๋์  peopleOnly ๋ณ์ ํ๋์ ์ ๋ ฌํ๋ค.

    for(i = 0; i < a.length; i++) {
        if(a[i] !== -1) {
            a[i] = peopleOnly.shift();
            //๋ฐ๋ก peopleOnly ์ฌ์ฉ
            //peopleOnly ์์๋ฅผ ์์๋๋ก a๋ฐฐ์ด ์์์ค -1์ด ์๋ ์์ ๋์  ๋ฃ๋๋ค.
        }
    }
    return a;
}
```

- splice ๋์  shift: [ ] ํด๋น ๋ฐฉ๋ฒ์ ์ฌ์ฉํ๋ ๋ชจ๋  ํ์คํธ์ ํฉ๊ฒฉํ๋ค. splice๋ฅผ ์ฐ๋ ๋ฐฉ๋ฒ์ด ์ข์ ๋ฐฉ๋ฒ์ ์๋ ๊ฒ ๊ฐ์๋ฐ, ๊ทธ ์ด์ ๋ฅผ ์ ์ ์์ผ๋ฉด ์ข๊ฒ ๋ค. ์ด ๋ถ๋ถ์ MDN์ ํด๋นํ๋ ๋ด์ฉ์ด ์๋์ง ์ฐพ์๋ด์ผ๊ฒ ๋ค.
- ๋ถํ์ํ ๋ณ์ ์ง์  ์ค์ด๊ธฐ : peopleOnly๋ก ์ฌ๋์ ํค๋ง ํฌํจํ ๋ฐฐ์ด์ ๋ง๋ค์๋ค๋ฉด, ์ด ๋ฐฐ์ด์ ์ ๋ ฌํด ์ฌ์ฉํ๋ฉด ๋๋ค. ๋ถํ์ํ๊ฒ sorted๋ผ๋ ์ ๋ ฌ๋ ๋ฐฐ์ด์ ๋ณ์๋ก ์ง์ ํด ์ฝ๋์์ ๊ฐ ๋ฐฐ์ด์ด ์ด๋ค ์ญํ ์ ํ๊ณ  ์๋์ง ์ดํดํ๊ธฐ ํ๋ค๋ค.
