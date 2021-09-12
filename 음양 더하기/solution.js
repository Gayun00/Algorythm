function solution(absolutes, signs) {
  const positiveNum = [];
  const negativeNum = [];

  for(let i = 0; i<signs.length; i++) {
    if(signs[i] === true) {
      positiveNum.push(absolutes[i])
    } else {
      negativeNum.push(absolutes[i])
    }
  }

  const sumPos = positiveNum.reduce((sum,el) => {
    return sum+el
  },0)
  const sumNeg = negativeNum.reduce((sum,el) => {
    return sum+el
  },0)

  const answer = sumPos - sumNeg
  return answer
}