function solution(n){
  let arr = [];
  let count = 0;
  for(k=2; k <= n; k++){
    arr = [];
    for(i=2; i < k; i++){
      
      arr.push(i);
    }

    const isPrime = arr.every((el)=>{
      return k % el !== 0;
    })

    if(isPrime)count++

  }
    let answer = count;
    return answer;
}

/**
 * 정확성 테스트
 * 테스트 10 〉	실패 (시간 초과)
 * 테스트 11 〉	실패 (시간 초과)
 * 테스트 12 〉	실패 (시간 초과)
 *
 * 효율성  테스트
 * 테스트 1 〉	실패 (시간 초과)
 * 테스트 2 〉	실패 (시간 초과)
 * 테스트 3 〉	실패 (시간 초과)
 * 테스트 4 〉	실패 (시간 초과)
 */