const readline = require('readline');
 
// 인터페이스 객체를 만들자.
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let arr = []

rl.on('line',line=>{
    if(!n){
        n = parseInt(line)
    }else{
        arr.push(line.split(' ').map(Number));
    }
    
}).on('close',()=>{
    // console.log(arr)
    arr.sort((a,b)=>{
        if(a[0] === b[0]){
            return a[1] - b[1]
        }
        return a[0] - b[0]
    })
    let cnt = 0;
    for(let [start,end] of arr){
        if(cnt <= start){
            cnt = start + end;
            // cnt += start+end;
        }else{
            cnt += end;
        }
    }
    console.log(cnt)
})