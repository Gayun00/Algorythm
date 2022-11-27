function solution(numbers, pick) {
  let ch = Array.from({length:numbers.length},() => 0);
  let answer = [];
  let count = 0;
  function dfs(level, result) {
    if(level === pick) {
      count++
      answer.push(result)
      console.log(count)
      return;
    } else {
      for(let i = 0; i < numbers.length; i++) {
        if(ch[i] === 0) {
          ch[i] = 1;
          dfs(level + 1, result + numbers[i]);
          ch[i] = 0;
        }
      }
    }

  }
  dfs(0,'')
  console.log([answer, count])
  return [answer, count]
}

solution([3,6,9], 2)