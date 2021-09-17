function solution(s) {
  return s.split(' ').map(word => {
      let result = '';
      for(let i = 0; i < word.length; i++) {
          if(i%2) {
              result += word[i].toLowerCase();
          } else {
              result += word[i].toUpperCase();
          }
      }
      return result;
  }).join(' ');
}
//원본배열에 적용시키기 힘들 때는 map을 사용하자.
