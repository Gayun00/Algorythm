
## ๐งช Description
Given a string s, find the length of the longest substring without repeating characters.

 

#### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
#### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
#### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, 
"pwke" is a subsequence and not a substring.
```
#### Example 4:
```
Input: s = ""
Output: 0
```

<br>


## ๐ Solution
```js
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0;
    let end = 0;
    let longest = 0;
    let set = new Set();
    
    while (start < s.length && end < s.length) {
        if(!set.has(s[end])) {
            set.add(s[end]);
            longest = Math.max(longest, end - start + 1);
            end++;
        } else {
            set.delete(s[start])
            start++;
        }
    }
    return longest;
};
```


[disscuss์๋ ํ์ด๋ฅผ ์ค๋ช๊ณผ ํจ๊ป ์ฌ๋ ค๋์๋ค](https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1567344/js-easy-sliding-window-solution-with-explanation)

1. end pointer๋ฅผ ์ด๋ํด๊ฐ๋ฉฐ ํด๋น ์ํ๋ฒณ์ด set์ ๋ค์ด์๋์ง ํ์ธํ๋ค.
2. ์์ ๊ฒฝ์ฐ์ ์ํ๋ฒณ์ set์ ๋ฃ๋๋ค.
3. end์ start ํฌ์ธํฐ๊ฐ์ ๊ฑฐ๋ฆฌ๋ฅผ ๊ตฌํ๋ค. ์ด ๊ฑฐ๋ฆฌ๋ ๋งค๋ฒ ๊ตฌํ ๋ค์ ์ต๋๊ฐ์ longest์ ํ ๋นํด์ค๋ค. ๊ฐ์ฅ ๊ธด ๊ฑฐ๋ฆฌ๋ฅผ ์ฐพ๊ธฐ ์ํจ์ด๋ค.
4. end pointer++๋ก ํ์นธ ์ด๋ํด์ค๋ค.
5. set์ ๊ฐ์ ์ํ๋ฒณ์ด ๋ค์ด์๋ค๋ฉด set์์ ๊ทธ ์ํ๋ฒณ์ ์ญ์ ํ๋ค.
   set'abc'์์ 'a'๋ฅผ ์ญ์ ํด์ฃผ๋ฉด, endpointer๊ฐ s=abcabcbb์์ abc์ ๋ค์ 'a'๋ฅผ ์ง์ด๋ฃ๋๋ค. set์ 'bca'๊ฐ ๋๋ค. startํฌ์ธํฐ๋++๋์ด sliding window๋ 'bca'๋ก ์ด๋ํ๊ณ , ์ค๋ณต๋๋ ์ํ๋ฒณ์ ๋ฐ๋ผ๋ณด์ง ์๋๋ค.
6. ๋ ํฌ์ธํฐ๊ฐ ๋์ ๋๋ฌํ  ๋๊น์ง ๊ณผ์ ์ ๋ฐ๋ณตํ๊ณ , ๊ฐ์ฅ ์ต๋๊ฐ์ธ longest๋ฅผ ๋ฐํํ๋ค.
   ![](https://images.velog.io/images/gygy/post/134de295-1f30-4719-9043-5768b58805f2/image.png)

<br>

## ๐งซ Result
#### Runtime
92 ms, faster than 94.88% of JavaScript online submissions for Longest Substring Without Repeating Characters.
#### Memory Usage
43.1 MB, less than 79.71% of JavaScript online submissions for Longest Substring Without Repeating Characters.

<br>

> hash set์ ์ต์ํ์ง ์์๊ณ , sliding window์ ๊ฐ๋๋ ์ฒ์ ์ ํด์ ์ฒ์์ ์กฐ๊ธ ํค๋งธ๋ค. ๊ทธ๋๋ ๋ค๋ฅธ ํ์ด๋ฅผ ๋ฒ ๋ผ์ง ์๊ณ  ์ค์ค๋ก ํ์ด์ ๋ณด๋์ ์๋ค!! ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ
