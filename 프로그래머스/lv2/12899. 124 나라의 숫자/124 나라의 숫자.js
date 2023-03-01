function solution(n) {
    let answer = '';
    const numArr = [4, 1, 2];
    
    while(n) {
        answer = numArr[n%3] + answer;
        // 0 == false
        n = n%3 === 0 ? n/3 -1 : Math.floor(n/3); 
    }
     
    return answer;
}