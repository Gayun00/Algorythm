## πλ¬Έμ 
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
1 β€ statues.length β€ 10,
0 β€ statues[i] β€ 20.

[output] integer

The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.

## πSolution
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

λ€ νκ³  λμ μκ°ν΄λ³΄λ, ν¨μ¨μ μ΄μ§ μμλ€. λΉ μ Έμλ μ«μλ₯Ό λ¦¬ν΄ν  νμ μμ΄ κ°―μλ§ κ³μ°νλ©΄ λλ κ²μ΄μκΈ° λλ¬Έμ... μ²μμ μκ°νλ λλ‘ μ°μλμ§ μμ μ«μκ° μλ€λ©΄ μΉ΄μ΄νΈ +1λ§ ν΄μ£Όλ©΄ λμλ€.
