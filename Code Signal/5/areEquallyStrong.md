## πλ¬Έμ 
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

## πνμ΄
```js
function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
    const yourStrength = [yourLeft, yourRight];
    const friendsStrength = [friendsLeft, friendsRight];

   return Math.max(...yourStrength) === Math.max(...friendsStrength)
    && Math.min(...yourStrength) === Math.min(...friendsStrength)
    ? true : false;
}

```

## β¨λ€λ₯Έ νμ΄
```js
function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
    var me = [yourLeft, yourRight].sort().join("");
    var friend = [friendsLeft, friendsRight].sort().join("");

    return me === friend;
}
```

νΉλ²ν λ μ’μ νμ΄μΈμ§λ λͺ¨λ₯΄κ² λ€.
κ°μ₯ λ¬΄κ±°μ΄ λ¬΄κ²μ κ°λ²Όμ΄ λ¬΄κ²κ° κ°μμΌ νλλ° μ νμ§λ λκ°μ΄κΈ° λλ¬Έμ, λ€λ₯Έ νμ΄μ²λΌ μμλ₯Ό μμ κ³  λ κ°μ κ°μ΄ λͺ¨λ κ°μΌλ©΄ trueλ‘ λ¦¬ν΄ν΄λ λλ€.
νμ§λ§ 2κ°μ κ°μ΄ μλ κ²½μ°λ₯Ό μκ°νμ λ, μ΅λκ°κ³Ό μ΅μκ°μ κ°κ° κ΅¬νλ λ°©λ²μ΄ μ μμΈ κ² κ°λ€.
