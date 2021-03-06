## ๐Problem
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

#### Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:



![](https://images.velog.io/images/gygy/post/c252b591-7778-4a4b-a643-2746c123ba46/image.png)


## ๐KeyPoint
์ฅ์ ๋ฌผ์ ํผํ๊ธฐ ์ํด์๋ `์ฝ์`๊ฐ ์๋ ์ซ์๋งํผ ๋ฐ์ด๋์ด์ผ ํ๋ค.
๋ฐ์ด๋๋ ๊ฑฐ๋ฆฌ๋ฅผ x๋ผ๊ณ  ํ์ ๋, x=3์ด๋ฉด 3๊ณผ 6,9์ ์ฝ์์ด๋ฏ๋ก ๊ฐ๊ฐ์ ์ฅ์ ๋ฌผ์ ๋๋ฌํ์ฌ ๋ถ๋ชํ๊ฒ ๋๋ค.
๊ฒฐ๊ตญ ๋ชจ๋  inputArray ์์์ ์ฝ์๊ฐ ์๋ ์ซ์๋ฅผ ์ฐพ์ผ๋ฉด ๋๋ค.

## ๐Solution
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
1. inputArray์ ๋ชจ๋  ์์๋ฅผ ๋๋ฉด์ x๋ก ๋๋์ด๋ณธ๋ค. 
2. ํ ์์๋ผ๋ x๋ก ๋๋์์ ๋ ๋๋จธ์ง๊ฐ 0์ด๋ฉด x๊ฐ ๊ทธ ์์์ ์ฝ์๋ผ๋ ๋ป์ด๋ฏ๋ก x๋ฅผ +1ํ๋ค.
3. ๋ฐ๋ณตํ๋ค.
4. ์ด๋ค ์์๋ x๋ก ๋๋์ด๋จ์ด์ง์ง ์์ ๋, x๋ inputArray์ ๋ชจ๋  ์์์ ์ฝ์๊ฐ ์๋๋ฏ๋ก ์ฅ์ ๋ฌผ์ ๋ชจ๋ ํผํ  ์ ์๋ค.