function solution(n) {
  return Number.parseInt(String(n)
      .split('')
      .sort((a, b)=>{return b - a})
      .join(''))
}
