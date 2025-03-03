function solution(name, yearning, photo) {
    var answer = [];
    let obj = {}
    for(let i =0; i <name.length ; i++){
        obj[name[i]] = yearning[i];
    }
    
    for(let i =0; i < photo.length; i ++){
        let cnt = 0;
        for(let n of photo[i]){
            if(obj[n]){
                cnt += obj[n]
            }
        }
        answer.push(cnt)
    }
    return answer;
}