//정렬을 사용한 방법은 불가능 해 수정
function solution(arr) {
  let arr2 = arr;
  const min = Math.min(...arr2);
  const minIndex = arr2.indexOf(min);
  arr2.splice(minIndex,1)

  if(arr2.length === 0) return [-1];

return arr2;
};
