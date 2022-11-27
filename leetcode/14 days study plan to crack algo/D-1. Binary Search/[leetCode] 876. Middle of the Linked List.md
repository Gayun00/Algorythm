## 🧪 Description
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

#### Example 1:

![](https://images.velog.io/images/gygy/post/0d926888-441e-4159-aed2-34fba7786cde/image.png)
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```
#### Example 2:

![](https://images.velog.io/images/gygy/post/85cbe7cf-423e-4999-a73e-cec921ed04e1/image.png)
```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```
## 💊 Solution
이번 문제는 연결리스트를 사용하는 문제였다.
자료구조인 연결리스트가 무엇인지,
연결리스트는 어떻게 접근해야 하는지를 알아야 한다.


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
 * @return {ListNode}
 */
var middleNode = function(head) {
    let slow = head;
    let fast = head;
    while(fast !== null) {
        fast = fast.next;
        if (fast === null) break;
        else {
            fast = fast.next;
        }
        slow = slow.next;
    }
    return slow;
};
```

## 🧫 Result
#### Runtime
76 ms, faster than 57.09% of JavaScript online submissions for Middle of the Linked List.
#### Memory Usage
39.2 MB, less than 7.70% of JavaScript online submissions for Middle of the Linked List.
