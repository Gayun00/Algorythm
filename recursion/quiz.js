/*## Quiz

출처 : [https://ko.javascript.info/recursion](https://ko.javascript.info/recursion)

### ****[주어진 숫자까지의 모든 숫자 더하기](https://ko.javascript.info/recursion#ref-1077)****

중요도: 5

숫자 `1 + 2 + ... + n`을 계산하는 함수 `sumTo (n)`을 만들어보세요.

예시:

```jsx
sumTo(1) = 1
sumTo(2) = 2 + 1 = 3
sumTo(3) = 3 + 2 + 1 = 6
sumTo(4) = 4 + 3 + 2 + 1 = 10
...
sumTo(100) = 100 + 99 + ... + 2 + 1 = 5050
```

아래 방법을 사용해 세 가지 답안을 만들어보세요.

- for 반복문 사용하기
*/
    
    function sumTo(n) {
    	let sum = 0;
    	for(i=1; i<=n; i++){
    		sum += i;
        }
    	return sum;
    }
    

//- 재귀 사용하기(`n > 1`일 때 `sumTo(n) = n + sumTo(n-1)`)

    function sumTo(n) {
      if (n == 1) return 1;
      return n + sumTo(n - 1);
    }

//- [등차수열](https://en.wikipedia.org/wiki/Arithmetic_progression) 공식 사용하기

    function sumTo(n) {
      return n * (n + 1) / 2;
    }

//### 팩토리얼

//재귀를 사용하여 n!을 계산하는 함수, factorial(n)을 만들어보세요.

function factorial(n) { 
	if(n === 1) return 1;
	return n * factorial(n-1);
}

//좀 더 간결한 코드 :
return (n != 1) ? n * factorial(n - 1) : 1;

/*### 피보나치 수

[피보나치 수](https://ko.wikipedia.org/wiki/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98_%EC%88%98)는 첫째와 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열로, `Fn = Fn-1 + Fn-2`라는 공식으로 표현할 수 있습니다.

처음 두 항은 `1`이고, 그다음 항들은 `2(1+1)`,`3(1+2)`,`5(2+3)`이므로 전체 수열은 `1, 1, 2, 3, 5 , 8, 13, 21 ...` 형태를 띱니다.

- 재귀 함수
*/
    function fibonacci(n) {
    	if(n === 1 || n === 2) return 1;
    	return fibonacci(n-1) + fibonacci(n-2);
    }

    //더 간결한 코드 :
    function fib(n) {
      return n <= 1 ? n : fib(n - 1) + fib(n - 2);
    }

//    이렇게 하면.... 수많은 서브 호출이 일어나 콜스택이 쌓이고 CPU리소스를 많이 잡아먹게 되어 처리속도가 느려진다.

//- 반복문

    function fib(n) {
      let a = 1;
      let b = 1;
      for (let i = 3; i <= n; i++) {
        let c = a + b;
        a = b;
        b = c;
      }
      return b;
    }
