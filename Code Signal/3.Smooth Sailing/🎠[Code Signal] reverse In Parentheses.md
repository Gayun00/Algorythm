## ๐๋ฌธ์ 
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

#### Example

For `inputString = "(bar)"`, the output should be
`reverseInParentheses(inputString) = "rab"`;
For `inputString = "foo(bar)baz"`, the output should be
`reverseInParentheses(inputString) = "foorabbaz";`
For `inputString = "foo(bar)baz(blim)"`, the output should be
`reverseInParentheses(inputString) = "foorabbazmilb"`;`
For `inputString = "foo(bar(baz))blim"`, the output should be
`reverseInParentheses(inputString) = "foobazrabblim"`.
Because `"foo(bar(baz))blim"` becomes `"foo(barzab)blim"` and then `"foobazrabblim"`.




## โจ๋ค๋ฅธ ํ์ด

์ ๊ทํํ์์ผ๋ก ํ์ด๋ณด๋ ค ํ๋๋ฐ, (baz)์ ๊ฐ์ด ๊ดํธ๊น์ง ํฌํจ๋ ๋ฌธ์๋ฅผ ๊ฐ์ ธ์๋ค.
๊ฐ์ด ์ ์์ ๊ณ ๋ฏผํ๋ค๊ฐ ๋ค๋ฅธ ํ์ด๋ฅผ ์ดํด๋ดค๋ค.

``` js
function reverseInParentheses(inputString) {
    while (inputString.includes('(')) {
        inputString = inputString.replace(/\(([^()]*)\)/, (_, str) => [...str].reverse().join(''));
    }
    return inputString;
}
```

## ๐กReview
### ์ ๊ทํํ์
- ์ถ๊ฐ ์์ 



