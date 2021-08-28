function solution(price, money, count) {
    var answer = -1;
    arr=[];
    for(i=0; i<count; i++){
    arr.push(price*(count-i))
    }     
             
    var result = arr.reduce(function sum(a,b){
        return a + b
    })
    
    if((result-money)>0){
        var answer = result-money
        }
    else{
        var answer = 0
    }
    return answer;
}