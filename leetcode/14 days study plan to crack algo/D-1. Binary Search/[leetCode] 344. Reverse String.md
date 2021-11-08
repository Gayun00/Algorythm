## 🎆 Description

```
Write a function that reverses a string. The input string is given as an array of characters s.
```
 

#### Example 1:
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```
#### Example 2:
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

<br>

## 🎇 Solution

```js
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let low = 0;
    let high = s.length - 1;
    let save;
    while (low < high) {
        save = s[high];
        s[high] = s[low];
        s[low] = save;
        
        high--;
        low++;
    }
    return s;
};
```

- 양쪽이 바뀌어야하기 떄문에 맨 끝에 포인터를 둔다.
- 가운데로 각각 이동하면서 서로 문자를 바꾸어준다.
- 한 번 high에 low의 값을 할당하면 high의 값은 없어지기 때문에 미리 새로운 변수에 high의 값을 할당해놓은 다음, low에 이 변수의 값을 다시 할당해주는 방식으로 서로의 값을 바꾼다.

>이제 two pointers를 사용해 알고리즘을 푸는 건 많이 익숙해진 것 같다!
