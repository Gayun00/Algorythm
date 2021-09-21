function solution(x, n) {
  const arr = [];
  let f = 0;
  for (i=0; i < n; i++) {
      f += x ;
      arr.push(f);
  }
  return arr;
}