### 🎆Problem
Check if all digits of the given integer are even.

`Example`

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
<br>

### 🎇Solution
```js
function evenDigitsOnly(n) {
    const arr = String(n).split('');
    const nums = [];
    arr.forEach((el) => {
        nums.push(Number.parseInt(el));
    
    })
    
    return nums.every(num => num % 2 === 0) ? true : false;
    
}
```

## Reference
https://app.codesignal.com/