## 🎆문제
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

#### Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

#### Input/Output

[execution time limit] 4 seconds (js)

[input] array.integer statues

An array of distinct non-negative integers.

Guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.

[output] integer

The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.

## 🎆Solution
```js
function makeArrayConsecutive2(statues) {
    const sorted = statues.sort((a,b) => {return a-b});
    const first = sorted[0];
    const last = sorted[sorted.length-1];
    let result = [];
    let baseArr = [];

    for(i=first;i<=last;i++) {
        baseArr.push(i);
    }

    baseArr.forEach((el) => {
        if(!sorted.includes(el)) {
            result.push(el);
        }
    });

    return result.length;
}
```

다 풀고 나서 생각해보니, 효율적이지 않았다. 빠져있는 숫자를 리턴할 필요 없이 갯수만 계산하면 되는 것이었기 때문에... 처음에 생각했던 대로 연속되지 않은 숫자가 있다면 카운트 +1만 해주면 되었다.
