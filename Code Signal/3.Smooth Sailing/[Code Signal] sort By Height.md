## 🎆문제
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

#### Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

## 🎇풀이 - Hidden Test 1개 실패

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
Hidden Test 한 문항을 통과하지 못했다.. 어떤 것 때문일까?

## ✨다른 풀이
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
- 여기에선 shift()메서드를 사용했다.
aFiltered에는 -1을 제외한 사람의 키만 넣어두었는데, aFiltered.shift()는 첫번째 요소 하나를 배열에서 제거 한 후 이 요소를 반환한다. 원본 배열 중 -1이 아닌 요소를 제거 한 뒤 반환된 aFiltered의 첫번째 요소로 대체하는 것을 반복한다.
즉, aFiltered의 첫번째 요소는 계속 제거 되니 for문이 돌 때마다 차례대로 모든 요소를 거치므로, 정렬된 배열의 요소들로 순차적으로 원본 배열의 -1이 아닌 요소들을 대체시킨다.

### 다시 풀어보았다. 해결!
```js
function sortByHeight(a) {

    if(a.every((el) => {return el === -1})){return a}

    let peopleOnly = [];
    peopleOnly = a.filter((el) => {
        return el !== -1
    }).sort((a,b) => {return a - b});
    //굳이 필요없는 sorted 변수 지정 대신 peopleOnly 변수 하나에 정렬했다.

    for(i = 0; i < a.length; i++) {
        if(a[i] !== -1) {
            a[i] = peopleOnly.shift();
            //바로 peopleOnly 사용
            //peopleOnly 요소를 순서대로 a배열 요소중 -1이 아닌 요소 대신 넣는다.
        }
    }
    return a;
}
```

- splice 대신 shift: [ ] 해당 방법을 사용하니 모든 테스트에 합격했다. splice를 쓰는 방법이 좋은 방법은 아닌 것 같은데, 그 이유를 알 수 있으면 좋겠다. 이 부분은 MDN에 해당하는 내용이 있는지 찾아봐야겠다.
- 불필요한 변수 지정 줄이기 : peopleOnly로 사람의 키만 포함한 배열을 만들었다면, 이 배열을 정렬해 사용하면 된다. 불필요하게 sorted라는 정렬된 배열을 변수로 지정해 코드에서 각 배열이 어떤 역할을 하고 있는지 이해하기 힘들다.
