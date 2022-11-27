
## 🧪 Description
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


## 💊 Solution
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


[disscuss에도 풀이를 설명과 함께 올려두었다](https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1567344/js-easy-sliding-window-solution-with-explanation)

1. end pointer를 이동해가며 해당 알파벳이 set에 들어있는지 확인한다.
2. 없을 경우에 알파벳을 set에 넣는다.
3. end와 start 포인터간의 거리를 구한다. 이 거리는 매번 구한 다음 최댓값을 longest에 할당해준다. 가장 긴 거리를 찾기 위함이다.
4. end pointer++로 한칸 이동해준다.
5. set에 같은 알파벳이 들어있다면 set에서 그 알파벳을 삭제한다.
   set'abc'에서 'a'를 삭제해주면, endpointer가 s=abcabcbb에서 abc의 다음 'a'를 집어넣는다. set은 'bca'가 된다. start포인터는++되어 sliding window는 'bca'로 이동하고, 중복되는 알파벳을 바라보지 않는다.
6. 두 포인터가 끝에 도달할 떄까지 과정을 반복하고, 가장 최댓값인 longest를 반환한다.
   ![](https://images.velog.io/images/gygy/post/134de295-1f30-4719-9043-5768b58805f2/image.png)

<br>

## 🧫 Result
#### Runtime
92 ms, faster than 94.88% of JavaScript online submissions for Longest Substring Without Repeating Characters.
#### Memory Usage
43.1 MB, less than 79.71% of JavaScript online submissions for Longest Substring Without Repeating Characters.

<br>

> hash set에 익숙하지 않았고, sliding window의 개념도 처음 접해서 처음에 조금 헤맸다. 그래도 다른 풀이를 베끼지 않고 스스로 풀어서 보람은 있다!! 🔥🔥🔥🔥🔥🔥
