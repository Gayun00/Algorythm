function solution(numbers) {
  const nums = [1,2,3,4,5,6,7,8,9];
  const sortedNumbers = numbers.sort();

  for(i = 0; i < nums.length; i++) {
      for(j = 0; j < numbers.length; j++) {
          if(nums[i] === sortedNumbers[j]) {
              nums.splice(i,1);
          }
      }
  }
  const sum = nums.reduce((sum,curr) => {
      return sum + curr;
  });
}

/**
 * 다른풀이 1.
 *
 * function solution(numbers) {
    let cnt = 0;
    for(let i=0; i<10; i++){
        if(!(numbers.includes(i))) cnt+= i
    }
    return cnt

}
 *
 * 다른풀이 2.
 *
 * function solution(numbers) {
    return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}
 *
 *
 */