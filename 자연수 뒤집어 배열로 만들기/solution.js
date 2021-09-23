//[실패] 첫번째 풀이: sort()사용

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

//[통과] 두번째 풀이: reverse()사용

function solution(n) {
  const arr = [];
  String(n).split('').forEach((el) => {
      arr.push(Number.parseInt(el));
  });
  return arr.reverse();
}
