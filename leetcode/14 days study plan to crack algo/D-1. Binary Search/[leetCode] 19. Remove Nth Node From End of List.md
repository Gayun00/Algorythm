## ๐งช Description
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

#### Example 1:
![](https://images.velog.io/images/gygy/post/e2b05652-9172-4b3e-ab1b-9ec40b86dbf9/image.png)
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
#### Example 2:
```
Input: head = [1], n = 1
Output: []
```
#### Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
```

<br>
<br>

## ๐ Solution

๊ธฐ๋ณธ์ ์ธ ์๋ฆฌ๋ ๋ค์๊ณผ ๊ฐ๋ค. Description์ Example1์ผ๋ก ์ดํด๋ณด์.

![](https://images.velog.io/images/gygy/post/6d859d5a-6053-4f2d-a628-587a4eaf12c3/KakaoTalk_20211108_134705157.jpg)


1. ๋์์ n๋ฒ์งธ ๋ธ๋๋ฅผ ์ฐพ์์ผ ํ๋๊น, fast ํฌ์ธํฐ๋ฅผ ๋จผ์  n๋งํผ ์ด๋์์ผ๋๋๋ค.
2. fast๊ฐ ๋์ ๋๋ฌํ  ๋๊น์ง slow์ fastํฌ์ธํฐ๋ฅผ ๋๊ฐ์ด 1์ฉ ์ด๋์ํค๋ฉด slow๋ ์ ๊ฑฐํด์ผํ  n๋ฒ์งธ ๋ธ๋ ๋ฐ๋ก ์ด์ ์ ์์นํ๊ฒ ๋๋ค.
3. ์์์ด๋ฏธ์ง๋ก ์๋ฅผ๋ค๋ฉด, 
```
slow = [3,4,5]
slow.next = [4,5] 
slow.next.next = [5]
```
์ด๋ค.
`slow.next = slow.next.next`๋ก slow๋ค์์ด ๋ฐ๋ก [5]๊ฐ ๋๋๋ก ๋ง๋ค๋ฉด ์ค๊ฐ์ ๋ธ๋ 4๋ ์ญ์ ๋๊ณ  [1,2,3,5] ์ฐ๊ฒฐ๋ฆฌ์คํธ๊ฐ ๋ฐํ๋๋ค.

<br>

### โ 1st approach - run time error
```js
var removeNthFromEnd = function(head, n) {
    let slow = head;
    let fast = head;

    while (n > 0) {
        n--;
        fast = fast.next;

    }
    
    
    while (fast.next !== null) {
        fast = fast.next;
        slow = slow.next;
    }
    
    slow.next = slow.next.next;
    
    return head;
    
};
```


์ฌ๊ธฐ์ ๋ฌธ์ ๋ ๊ธธ์ด๊ฐ 1์ธ ์ฐ๊ฒฐ๋ฆฌ์คํธ์ ํ์คํธ์ผ์ด์ค๋ฅผ ํต๊ณผํ์ง ๋ชปํ๋ค๋ ๊ฒ์ด์๋ค.
```
Line 24 in solution.js
    while (fast.next !== null) {
                ^
TypeError: Cannot read property 'next' of null
      
Input: head = [1], n = 1
Output: []// ๋ด ๋ต์์ ๊ฒฐ๊ณผ๋ [1] ์ด์๋ค.
```
n๋ ๊ทธ๋๋ก 1์ด๊ณ ,
๊ธธ์ด๊ฐ 1์ด๋ fast = fast.next๋ฅผ ํด์ค ์ ์์ด์ ๊ทธ๋๋ก 1์ด ๋จ์ ๊ฒฐ๊ณผ๋ก ๋ฐํ๋ ๊ฒ์ด๋ค.


<br>


### โญ 2nd approach
```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    nl = new ListNode(0);
    nl.next = head;
    let slow = nl;
    let fast = nl;

    while (n > 0) {
        n--;
        fast = fast.next;

    }
    
    while (fast.next !== null) {
        fast = fast.next;
        slow = slow.next;
    }
    
    slow.next = slow.next.next;
    
    return nl.next;
    
};
```

์์ฑ์ ํจ์๋ฅผ ์ด์ฉํด ListNode์ ์๋ก์ด ์ธ์คํด์ค nl์ ๋ง๋ ๋ค, ์ด๊ฒ์ ์ธ์๋ก ์ ๋ฌ๋ head์ฐ๊ฒฐ๋ฆฌ์คํธ์์ ๋ถ์ฌ์ฃผ์๋ค. ์ด๋ ๊ฒ ํ๋ฉด [1] ๊ณผ ๊ฐ์ด ํ๊ฐ์ ์์๋ง ๊ฐ์ง ์ฐ๊ฒฐ๋ฆฌ์คํธ๋ ์ด์ ์ nl์ด ์์ผ๋ nl.next๋ก 1์ ์ ๊ทผํ  ์ ์์ด ์๋ฌ๊ฐ ๋์ง ์๋๋ค.

๊ทธ๋ฆฌ๊ณ  ๋ฆฌํด ๋ํ nl.next๊ฐ์ผ๋ก ์ง์ ํด์ฃผ์๋ค.

<br>
<br>

## ๐งซ Result
#### Runtime
 64 ms, faster than 99.36% of JavaScript online submissions for Remove Nth Node From End of List.
#### Memory Usage
40.1 MB, less than 68.11% of JavaScript online submissions for Remove Nth Node From End of List.

>์ด๋ฒ ๋ฌธ์ ๋ ํธ๋๋ฐ ์ด๋ ค์์ ์๊ฐ์ด ๊ฝค ๊ฑธ๋ ธ๋ค. ์ญ์ ๋์ด๋ Medium.. ์ฐ๊ฒฐ๋ฆฌ์คํธ๋ผ๋ ๊ฐ๋ ์์ฒด๊ฐ ์์ํด์ ์ดํดํ๋๋ฐ ์๊ฐ์ด ๊ฑธ๋ ธ๋ค. 
๊ทธ๋๋ ๊ทธ๋งํผ ๋ฟ๋ฏํ ์๊ณ ๋ฆฌ์ฆ ํ์ด์๋ค!
