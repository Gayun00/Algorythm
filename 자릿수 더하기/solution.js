function solution(n){
  const arr = []
  const numArr = String(n).split('')

  numArr.forEach((el)=>{
    arr.push(Number.parseInt(el))
  })

  return arr.reduce((sum,curr) => {
      return sum + curr
  })
}
