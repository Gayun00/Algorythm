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
