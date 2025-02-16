function solution(n, s) {
    if(s < n) return [-1]
    var answer = [];
    let quotient = Math.floor(s / n)
    let remainder = s % n

    if(remainder === 0){
        for(let i = 0; i < n; i++) {
            answer.push(quotient)
        }
    }else if(remainder > 0){
        for(let j = 0; j < n; j++) {
            if(remainder > 0) {
                answer.push(quotient + 1)
                remainder--;
            }else if(remainder === 0) {
                answer.push(quotient)
            }else {
                break
            }
        }

    }

    return answer.sort((a,b) => a - b )
}
