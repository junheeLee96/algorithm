const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n,k;
let q12 = []
let q13 = [];
let q23 = [];


rl.on("line", (line) => {
    if(!n){
        [n,k] = line.split(' ').map(Number)
    }else{
        let [a,b,c] = (line.split(' ').map(Number))
        q12.push(a+b);
        q13.push(a+c);
        q23.push(b+c);
    }

}).on('close',()=>{
    q12.sort((a,b)=> b-a);
    q13.sort((a,b)=> b-a);
    q23.sort((a,b)=> b-a);
    q12.splice(k,2)
    q23.splice(k,2)
    q13.splice(k,2)

    let a =0, b=0, c=0;
    for(let i=0; i < k; i ++){
        a += q12[i];
        b += q13[i];
        c += q23[i]
    }
    console.log(Math.max(a,b,c))
})
