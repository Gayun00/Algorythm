## ๐๋ฌธ์ 
๋ ์ ์ A์ B๋ฅผ ์๋ ฅ๋ฐ์ ๋ค์, A+B๋ฅผ ์ถ๋ ฅํ๋ ํ๋ก๊ทธ๋จ์ ์์ฑํ์์ค.

์๋ ฅ
์ฒซ์งธ ์ค์ A์ B๊ฐ ์ฃผ์ด์ง๋ค. (0 < A, B < 10)

์ถ๋ ฅ
์ฒซ์งธ ์ค์ A+B๋ฅผ ์ถ๋ ฅํ๋ค.

์์  ์๋ ฅ 1
1 2
์์  ์ถ๋ ฅ 1
3

## ๐ํ์ด
์ด์  ์์ถ๋ ฅ ์ฝ๋๋ฅผ ์์ฑํด์ผ ํ๋ค.

```js
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a+b);

```

## ๐Review
- ์์ถ๋ ฅ์ :
`var fs = require('fs');`
`var input = fs.readFileSync('/dev/stdin').toString().split(' ');`
fs๋ฅผ ์์ฒญํ๋ค,์์ฒญํ์ฌ ๋ฌธ์์ด๋ก ๋ฐ๊พผ๋ค ๊ณต๋ฐฑ์ ๊ธฐ์ค์ผ๋ก ์๋ผ ๋ฐฐ์ด์ ๋ง๋ ๋ค.
