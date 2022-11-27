## 🎈문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A+B를 출력한다.

예제 입력 1
1 2
예제 출력 1
3

## 🎈풀이
이제 입출력 코드를 작성해야 한다.

```js
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a+b);

```

## 🎈Review
- 입출력시 :
`var fs = require('fs');`
`var input = fs.readFileSync('/dev/stdin').toString().split(' ');`
fs를 요청한뒤,요청하여 문자열로 바꾼뒤 공백을 기준으로 잘라 배열을 만든다.
