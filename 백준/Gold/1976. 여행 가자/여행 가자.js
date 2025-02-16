const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n,m;
let arr = []
let dist = []
let temp = 0;

rl.on("line", (line) => {
   if(!n){
       n = parseInt(line)
   }else if(!m){
       m =parseInt(line)
   }else if(temp < n ){
       temp ++;
       arr.push(line.split(' ').map(Number))
   }else{
       dist = line.split(' ').map(Number)
   }

}).on('close',()=>{
    let parent = Array.from({length:n+1},(_,i)=>i)
    for(let i = 0; i<n; i++){
        for(let j = 0; j < arr[i].length; j++){
            if(arr[i][j] === 1){
                union(parent,i+1,j+1)
            }
        }
    }
    let answer = 'YES'
    let now = dist[0];
    for(let i = 1 ; i <m; i++){
        if(parent[dist[i]] !== parent[now]){
            answer = 'NO';
            break
        }

        now = dist[i]
    }

    console.log(answer)

    function getParent(parent,x){
        if(parent[x] === x){
            return x;
        }
        return parent[x] = getParent(parent,parent[x])
    }

    function union(parent, x,y){
        let a = getParent(parent,x);
        let b = getParent(parent,y);

        if(a < b){
            parent[b] = a;
        }else{
            parent[a] = b;
        }
    }
    
})
