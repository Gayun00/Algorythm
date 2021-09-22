function solution(s) {
  return s.split(' ').map((word) => {
      result = '';
      for(i = 0; i < word.length; i++) {
          if(i%2) {
              result += word[i].toLowerCase();    
          } else {
              result += word[i].toUpperCase();
          }
      }
      return result;
  }).join(' ')
}
