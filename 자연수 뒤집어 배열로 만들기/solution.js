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

