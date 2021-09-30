## 🎆문제
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




## ✨다른 풀이

정규표현식으로 풀어보려 했는데, (baz)와 같이 괄호까지 포함된 문자를 가져왔다.
감이 안 와서 고민하다가 다른 풀이를 살펴봤다.

``` js
function reverseInParentheses(inputString) {
    while (inputString.includes('(')) {
        inputString = inputString.replace(/\(([^()]*)\)/, (_, str) => [...str].reverse().join(''));
    }
    return inputString;
}
```

## 🎡Review
### 정규표현식
- 추가 예정



