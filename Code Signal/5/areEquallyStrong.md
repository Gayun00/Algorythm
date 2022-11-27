## 🎆문제
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

#### Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.

## 🎇풀이
```js
function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
    const yourStrength = [yourLeft, yourRight];
    const friendsStrength = [friendsLeft, friendsRight];

   return Math.max(...yourStrength) === Math.max(...friendsStrength)
    && Math.min(...yourStrength) === Math.min(...friendsStrength)
    ? true : false;
}

```

## ✨다른 풀이
```js
function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
    var me = [yourLeft, yourRight].sort().join("");
    var friend = [friendsLeft, friendsRight].sort().join("");

    return me === friend;
}
```

특벌히 더 좋은 풀이인지는 모르겠다.
가장 무거운 무게와 가벼운 무게가 같아야 하는데 선택지는 두개이기 때문에, 다른 풀이처럼 순서를 없애고 두 개의 값이 모두 같으면 true로 리턴해도 된다.
하지만 2개의 값이 아닐 경우를 생각했을 때, 최댓값과 최솟값을 각각 구하는 방법이 정석인 것 같다.
