function solution(s) {
  let arr = [];
  s.split(' ').forEach((word)=>{
      for(i=0;i<word.length;i++) {
          if(i%2) {
              arr.push(word[i])
          } else {
              arr.push(word[i].toUpperCase())
          }
      }
      arr.push(' ')
  })
      const joined = arr.join('')
}
//map을 적극적으로 활용하자!!!
