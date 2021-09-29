## 🎆문제
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
![d](https://codesignal.s3.amazonaws.com/tasks/matrixElementsSum/img/example1.png?_tm=1624661706824)

example 2

Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it). Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.
(https://codesignal.s3.amazonaws.com/tasks/matrixElementsSum/img/example2.png?_tm=1624661707079)

## 🎇풀이
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
 * matrix[0][0] === 0이므로, 그 아래층 matrix[1][0], matrix[2][0] 은 탈락
 * matrix[1][2] === 0이므로, 그 아래층 matrix[2][2]는 탈락
 * 즉, matrix[i][j] === 0이라고 할 때 matrix[i+1][j], matrix[i+2][j]는 탈락이다.
 *
 * 한 층에 유령이 들어간 방을 찾고, x표시를 한다.
 */

```

## 🧨다른 풀이
```js
function matrixElementsSum(matrix) {
    var total = 0;

    // Navigate each column of rooms
    // i = current column, j = current floor in column
    for (var i = 0; i < matrix[0].length; i++) {
        for (var j = 0; j < matrix.length; j++) {
            if (matrix[j][i] === 0) {
                // This room is haunted, so we don't care about the rooms below it.
                // Continue to the next column of rooms
                break;
            }
            total += matrix[j][i];
        }
    }
    return total;
}
```
