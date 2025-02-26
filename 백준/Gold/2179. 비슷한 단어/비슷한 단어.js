const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let t ;
let arr = []
let temp = 0;
rl.on('line', (line) => {
    if(!t){
        t = parseInt(line)
    }else{
        arr.push({
            s:line,
            idx:temp,
        })
        temp++;
    }
    
}).on('close', () => {
    
    let answer = {
        cnt:0,
        s:[]
    }
    for(let i =0; i < t; i ++){
        for(let j=i+1; j < t; j++){
            const s1 = arr[i].s;
            const s2 = arr[j].s;
            let len = 0;
            let cnt = 0;
            let idx = 0;
            while(len < s1.length && len < s2.length ){
                if(s1[idx] !== s2[idx]) break;
                cnt++;
                idx ++;
            }
            if(answer.cnt < cnt){
                answer = {cnt, s:[s1,s2]}
            }
        }
    }
    console.log(answer.s[0])
    console.log(answer.s[1])
});
