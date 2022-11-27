## 🎆Problem
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

#### Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:



![](https://images.velog.io/images/gygy/post/c252b591-7778-4a4b-a643-2746c123ba46/image.png)


## 🎇KeyPoint
장애물을 피하기 위해서는 `약수`가 아닌 숫자만큼 뛰어넘어야 한다.
뛰어넘는 거리를 x라고 했을 때, x=3이면 3과 6,9의 약수이므로 각각의 장애물에 도달하여 부딪히게 된다.
결국 모든 inputArray 요소의 약수가 아닌 숫자를 찾으면 된다.

## 🎇Solution
```js
function avoidObstacles(inputArray) {
    let x = 2;
    while(inputArray.some((el)=> 
        el % x === 0)){
        x++;
    }
    return x;
}
```
1. inputArray의 모든 요소를 돌면서 x로 나누어본다. 
2. 한 요소라도 x로 나누었을 때 나머지가 0이면 x가 그 요소의 약수라는 뜻이므로 x를 +1한다.
3. 반복한다.
4. 어떤 요소도 x로 나누어떨어지지 않을 때, x는 inputArray의 모든 요소의 약수가 아니므로 장애물을 모두 피할 수 있다.