## ๐ Description

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

## ๐ Solution

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

- ์์ชฝ์ด ๋ฐ๋์ด์ผํ๊ธฐ ๋๋ฌธ์ ๋งจ ๋์ ํฌ์ธํฐ๋ฅผ ๋๋ค.
- ๊ฐ์ด๋ฐ๋ก ๊ฐ๊ฐ ์ด๋ํ๋ฉด์ ์๋ก ๋ฌธ์๋ฅผ ๋ฐ๊พธ์ด์ค๋ค.
- ํ ๋ฒ high์ low์ ๊ฐ์ ํ ๋นํ๋ฉด high์ ๊ฐ์ ์์ด์ง๊ธฐ ๋๋ฌธ์ ๋ฏธ๋ฆฌ ์๋ก์ด ๋ณ์์ high์ ๊ฐ์ ํ ๋นํด๋์ ๋ค์, low์ ์ด ๋ณ์์ ๊ฐ์ ๋ค์ ํ ๋นํด์ฃผ๋ ๋ฐฉ์์ผ๋ก ์๋ก์ ๊ฐ์ ๋ฐ๊พผ๋ค.

>์ด์  two pointers๋ฅผ ์ฌ์ฉํด ์๊ณ ๋ฆฌ์ฆ์ ํธ๋ ๊ฑด ๋ง์ด ์ต์ํด์ง ๊ฒ ๊ฐ๋ค!
