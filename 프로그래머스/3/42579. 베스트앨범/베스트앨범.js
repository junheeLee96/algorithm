function solution(genres, plays) {
    var answer = [];
    let obj={};
    for(let i=0; i <plays.length; i ++){
        if(!obj[genres[i]]){
            obj[genres[i]] = [plays[i], [[i,plays[i]]]];
        }else{
            obj[genres[i]][0] += plays[i];
            obj[genres[i]][1].push([i,plays[i]])
        }
    }
    let arr = Object.keys(obj).map(key=> obj[key]);
    arr.sort((a,b)=> b[0]-a[0]);
    for(let [w, sing] of arr){
        sing.sort((a,b)=> {
            if(b[1] === a[1]){
                return a[0]-b[0]
            }
            return b[1] - a[1]
        });
        answer.push(sing[0][0]);
        if(sing.length > 1){
            answer.push(sing[1][0])
        }
    }
    return answer;
}