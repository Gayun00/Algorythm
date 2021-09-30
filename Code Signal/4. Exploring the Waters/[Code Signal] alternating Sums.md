## 🎆문제
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

#### Example

For `a = [50, 60, 60, 45, 70]`, the output should be
`alternatingSums(a) = [180, 105]`.



## 🎇풀이
```js
function alternatingSums(a) {
    const team1 = [];
    const team2 = [];

    for(i = 0; i < a.length; i++) {
        if (i % 2) {
            team2.push(a[i]);
        } else {
            team1.push(a[i]);
        }
    }

    function sum(team) {
        return team.reduce((sum, curr) => {
            return sum + curr;
        },0)
    }
    return [sum(team1), sum(team2)];
}
```

## ✨다른 풀이
```js
alternatingSums = a =>
  a.reduce((p,v,i) => (p[i&1]+=v,p), [0,0])
```

## ✨다른 풀이 2
```js
function alternatingSums(a) {
    var team1 = 0;
    var team2 = 0;

    for (var i = 0; i < a.length; i++) {
        if (i % 2 == 0) {
            team1 += a[i];
        } else {
            team2 += a[i];
        }
    }

    return [team1, team2];
}
```
처음부터 숫자형을 사용했다. 배열로 처리할 필요 없이
`team1 += a[i]` 으로 바로 합계를 구해주면 된다.
