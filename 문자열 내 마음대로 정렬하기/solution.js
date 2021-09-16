function solution(strings, n) {
  const process = [];
  for(let property of strings) {
      const picked = property.substr(n,1)
      process.push(picked)
  }
  process.sort()
  
  for(let i = 0; i < strings.length; i++) {
      for(let j = 0; j < process.length; j++) {
          // console.log(arr[i],process[j])
          if(process[j].length === 1){
              if(arr[i].substr(n,1) === process[j]) {
              
                  process.splice(j,1,arr[i])
                  // console.log(process)
          }
          }
      }
  }
  const answer = process;
  return answer;

}