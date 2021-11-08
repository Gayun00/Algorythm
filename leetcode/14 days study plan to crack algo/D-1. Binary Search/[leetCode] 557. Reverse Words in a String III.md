## 🎆 Description
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

## 🎇 Solution
### ❌ 1st approach - time limit exceeded
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

>평소에 알고리즘을 풀면서 split메서드로 쪼개 배열을 만든다음 나중에 join으로 합쳐 리턴하는 방식으로 해결하는 경우가 많았는데, 이후에 다른 풀이법을 확인했을 때 더 효율적인 방법이 많았기 때문에 이와 같은 방식으로만 푸는것을 지양했었다.
하지만 이번 문제에서 일일히 변수를 생성해 할당하니 시간을 초과해서... 이 경우에는 나은 방법이 될 것 같았다.

<br>

### ⭕ 2nd approach
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

## 🎉 Result
#### Runtime 
92 ms, faster than 55.13% of JavaScript online submissions for Reverse Words in a String III.
#### Memory Usage
45.7 MB, less than 18.78% of JavaScript online submissions for Reverse Words in a String III.

>이번 풀이 방식은 효율이 떨어진다. 
14 days challenge에서의 가장 큰 목표는 각각 몰랐던 알고리즘 풀이방식을 익히는 것으로, 이번 문제는 two pointers로 꼭 풀어보고 싶었기 때문에 효율보다는 풀이 방식에 초점을 맞췄다.
