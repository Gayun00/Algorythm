function solution(left, right) {
  let count = 0;
  let evenArr = [];
  let oddArr = [];
  for(j = left; j <= right; j++){
      count = 0;
    for(i = 0; i <= right; i++){
      if(j % i === 0) {
        count++;
      }
    }
    if(count % 2 === 0) {
      evenArr.push(j);
    } else {
      oddArr.push(j);
    }
  }
  let evenSum = evenArr.reduce(
    (accum, curr)=>{
    return accum+curr;
  },0)
  let oddSum = oddArr.reduce(
    (accum, curr)=>{
    return accum+curr;
  },0)
  let answer = evenSum - oddSum;
  return answer;
 }
