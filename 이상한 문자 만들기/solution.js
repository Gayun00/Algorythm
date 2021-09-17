function solution(s) {
  const arr = [];
  const sliced = s.split(' ')
  sliced.forEach((el) => {
    for(i=0; i<el.length; i++) {
      if(i%2 ===0) {
        const upper = el[i].toUpperCase();
        arr.push(upper)
      } else {
        arr.push(el[i])
      }
    }
    con
  })
  return arr.join('')
}
//TrY HeLlO WoRlD 가 나와야 하는데,
//공백을 이미 잘라서 다시 넣어두기가 힘들다.
//sliced 원본 배열에는 변형이 없고, arr에는 단순히 각 글자를 push해서
//forEach문이 돌면서 단어별로 공백을 추가할 수 없다.
