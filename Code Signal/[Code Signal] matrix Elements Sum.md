## ๐๋ฌธ์ 
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

#### Example

For

```
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.
```
example 1

There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.

For
```
matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]
the output should be
matrixElementsSum(matrix) = 9.
```


example 2

Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it). Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.


## ๐ํ์ด
```js
function matrixElementsSum(matrix) {
    let rooms = matrix;
    let result = [];

    for(i = 0; i < rooms.length; i++) {
        for(j = 0; j < rooms[0].length; j++) {
            if(rooms[i][j] === 0 && i < rooms.length - 1) {
                rooms[i+1][j] = 0;
            } else if (rooms[i][j] !== 0){
                result.push(rooms[i][j]);
            }
        }
    }
    return result.reduce((sum,curr) => {
        return sum + curr;
    }, 0)
}
/**
 * ex 1)
 * matrix[0][0] === 0์ด๋ฏ๋ก, ๊ทธ ์๋์ธต matrix[1][0], matrix[2][0] ์ ํ๋ฝ
 * matrix[1][2] === 0์ด๋ฏ๋ก, ๊ทธ ์๋์ธต matrix[2][2]๋ ํ๋ฝ
 * ์ฆ, matrix[i][j] === 0์ด๋ผ๊ณ  ํ  ๋ matrix[i+1][j], matrix[i+2][j]๋ ํ๋ฝ์ด๋ค.
 *
 * ํ ์ธต์ ์ ๋ น์ด ๋ค์ด๊ฐ ๋ฐฉ์ ์ฐพ๊ณ , xํ์๋ฅผ ํ๋ค.
 */

```

## ๐งจ๋ค๋ฅธ ํ์ด
```js
function matrixElementsSum(matrix) {
    var total = 0;
    for (var i = 0; i < matrix[0].length; i++) {
        for (var j = 0; j < matrix.length; j++) {
            if (matrix[j][i] === 0) {
                break;
            }
            total += matrix[j][i];
        }
    }
    return total;
}
```

์ข ๋ ํจ์จ์ ์ธ ํ์ด์ด๋ค. ๋ค์ ์๊ณ ๋ฆฌ์ฆ ๋ฌธ์  ๋ ์ฐธ๊ณ ํ์! :

1. ์ผ์ผํ ๋ด ํ์ด์ฒ๋ผ 0์ผ๋ก ํ์ํ์ง ์๊ณ , break๋ก ๊ตฌ๋ฌธ ์ค๋จ
2. ์๋ก์ด ๋ฐฐ์ด์ ํธ์ํ ํ reduce๋ก ์ ์ฒด ๋ฐฐ์ด ์์ ํฉ๊ณ๋ฅผ ๊ตฌํ๋ ๋์  `total+=matrix[j][i]`์ฌ์ฉ
