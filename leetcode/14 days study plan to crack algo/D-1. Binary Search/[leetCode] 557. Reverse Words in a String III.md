## π Description
```
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
```
 

#### Example 1:
```
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```
#### Example 2:
```
Input: s = "God Ding"
Output: "doG gniD"

```
<br>
<br>

## π Solution
### β 1st approach - time limit exceeded
```js
var reverseWords = function(s) {
    let low = 0;
    let high = 0;
    let save;
    let firstHigh;
    
    while (low < s.length) {
        high = s.indexOf(' ', low) - 1;
       while(low < high) {
           firstHigh = high;
            save = s[high];
           s[high] = s[low];
           s[low] = save;
           low++;
           high--;
        }
    low = firstHigh + 2;
    }
};
```

>νμμ μκ³ λ¦¬μ¦μ νλ©΄μ splitλ©μλλ‘ μͺΌκ° λ°°μ΄μ λ§λ λ€μ λμ€μ joinμΌλ‘ ν©μ³ λ¦¬ν΄νλ λ°©μμΌλ‘ ν΄κ²°νλ κ²½μ°κ° λ§μλλ°, μ΄νμ λ€λ₯Έ νμ΄λ²μ νμΈνμ λ λ ν¨μ¨μ μΈ λ°©λ²μ΄ λ§μκΈ° λλ¬Έμ μ΄μ κ°μ λ°©μμΌλ‘λ§ νΈλκ²μ μ§μνμλ€.
νμ§λ§ μ΄λ² λ¬Έμ μμ μΌμΌν λ³μλ₯Ό μμ±ν΄ ν λΉνλ μκ°μ μ΄κ³Όν΄μ... μ΄ κ²½μ°μλ λμ λ°©λ²μ΄ λ  κ² κ°μλ€.

<br>

### β­ 2nd approach
```js
var reverseWords = function(s) {
    const arr = s.split(' ');
    
    let low = 0;
    let high;
    let save;
    let answer = [];
    
    for (a of arr) {
        let as = a.split('')
        high = as.length - 1;
        low = 0;
        
        while (low < high) {
            save = as[low];
            as[low] = as[high];
            as[high] = save;
            low++;
            high--;        
        }
        answer.push(as.join(''));
    }
    return answer.join(' ')
};
```
<br>
<br>

## π Result
#### Runtime 
92 ms, faster than 55.13% of JavaScript online submissions for Reverse Words in a String III.
#### Memory Usage
45.7 MB, less than 18.78% of JavaScript online submissions for Reverse Words in a String III.

>μ΄λ² νμ΄ λ°©μμ ν¨μ¨μ΄ λ¨μ΄μ§λ€. 
14 days challengeμμμ κ°μ₯ ν° λͺ©νλ κ°κ° λͺ°λλ μκ³ λ¦¬μ¦ νμ΄λ°©μμ μ΅νλ κ²μΌλ‘, μ΄λ² λ¬Έμ λ two pointersλ‘ κΌ­ νμ΄λ³΄κ³  μΆμκΈ° λλ¬Έμ ν¨μ¨λ³΄λ€λ νμ΄ λ°©μμ μ΄μ μ λ§μ·λ€.
