function solution(arr) {
    let arr2 = arr;
    const sorted = arr2.sort((a,b)=>b-a);
    const removed = sorted.splice(arr2.length-1,1)
    if(arr2.length !==0) {
        return arr2;
    } else{
        arr2 = [-1];
        return arr2;
    }      
};
