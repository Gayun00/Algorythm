/*Test Case
scores = [
    [100,90,98,88,65],
    [50,45,99,85,77],
    [47,88,95,80,67],
    [61,57,100,80,65],
    [24,90,94,75,65]
]
    

scores = [
    [50,90],
    [50,87]
]


scores = [[70,49,90],[68,50,38],[73,31,100]]
*/

function solution(scores){
    scores2=[];
    for(j=0; j<scores.length; j++){
    scores1=[];
    for(i=0; i<scores.length; i++){
        scores1.push(scores[i][j])
        
    }
    scores2.push(scores1)
    console.log(scores2)
        
    }
    const result =[];
    for(i=0;i<scores2.length;i++){
        if(scores2[i][i] === Math.max(...scores2[i])
        ||scores2[i][i] === Math.min(...scores2[i])){
            scores2[i].splice(i,1)
        }
        console.log(scores2[i])

        const sum = scores2[i].reduce(function add(a,b){
                return a+b
        },0)
        const average = sum/scores2[i].length
                console.log(average);
        
        if(90<=average){
            result.push("A")
        }else if(80<=average){
            result.push("B")
        }else if(70<=average){
            result.push("C")
        }else if(50<=average){
            result.push("D")
        }else{
            result.push("F")
        }
        console.log(result)
        
    }
    const answer = result.join('')
    return answer;

}