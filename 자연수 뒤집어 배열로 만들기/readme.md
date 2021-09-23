# 자연수 뒤집어 배열로 만들기
## 문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

## 제한 조건
n은 10,000,000,000이하인 자연수입니다.
## 입출력 예
n	return
12345	[5,4,3,2,1]


# 풀이
### 첫번째 풀이
첫 번째 풀이는 통과되지 않았는데, 그 이유를 찾았다.
sort()를 사용해 내림차순으로 정렬하는 것이 아닌, 그대로 순서를 뒤집는 것이다.
예를 들어 12472를 넣으면 27421순으로 출력되어야 한다.
```
function solution(n) {
  const arr = [];
  String(n).split('').forEach((el) => {
      arr.push(Number.parseInt(el))
  })
  const sorted = arr.sort((a,b)=>{
      if(a > b) return -1;
      if(a === b) return 0;
      if(a < b) return 1})
  return sorted
}
```

### 두번째 풀이
reverse()를 사용해 그대로 뒤집어주었다.
```
function solution(n) {
    const arr = [];
    String(n).split('').forEach((el) => {
        arr.push(Number.parseInt(el));
    });
    return arr.reverse();
}
```

# Review
## reverse()
Array.prototype.reverse()는 배열을 반전시킨다.
원본 배열을 변형하여 참조값을 반환한다.

```
a.reverse();
console.log(a); // [3, 2, 1]
```
