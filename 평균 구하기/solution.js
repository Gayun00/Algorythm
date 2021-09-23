function solution(arr) {
  return arr.reduce((sum, curr) => {
      return sum + curr;
  }) / arr.length;
}
