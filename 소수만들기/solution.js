function solution(nums) {   
    arr = [1,2,3,4]
    let results = [];
    let count = [];
    for(let i = 0; i<nums.length; i++) {
        for(let j = i+1; j<nums.length; j++) {
            for(let k = j+1; k<nums.length; k++){
      
                results = [nums[i],nums[j],nums[k]]
      console.log(results)
                const resultsSum = results.reduce((sum,curr) => {
                    return sum+curr;
                },0)
      console.log(resultsSum)
      
                if(isPrime(resultsSum)) {
                    count++;
      
                }
      
            }
        }
    function isPrime(number) {
        if(number === 2)
            return true;

        for(let i = 2; i<=number/2; i++){
            if(number % i === 0){
                return false;
            }
        }
        return true;
    }
    const answer = count;
    return answer;
}
}