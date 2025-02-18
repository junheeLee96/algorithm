const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let arr = []
let n,m;
let temp = 0;
let camera = []
let cameras = 0
let answer = 0;
let wall = 0
rl.on("line", (line) => {
    if(!n){
        [n,m] = line.split(' ').map(Number)
    }else{
        const row = line.split(' ').map(Number)

        for(let i =0; i < m; i++){
            if(row[i] >= 1 && row[i] < 6){
                camera.push([temp,i]);
                cameras++;
            }
            if(row[i] === 6){
                wall ++;
            }
        }
        arr.push(row)
        temp ++;
    }
  
}).on("close", () => {
    // console.log('cameras = ',cameras, 'wall = ',wall, 'n*m =',n*m)
    dfs(0,[])
    console.log(n*m - (wall + cameras + answer))
});


function checking(dp,x,y,dir){
    let nx = x;
    let ny = y;
    let cnt = 0;
    
    while(0 <= nx && nx < n && 0 <= ny && ny < m){
        if(arr[nx][ny] === 6){
            return cnt
        }
        if(dp[nx][ny] === 0 && arr[nx][ny] === 0){
        dp[nx][ny] = 1
         cnt ++;   
        }
        if(dir === 0){
            nx --;
        }else if(dir === 1){
            ny ++;
        }else if(dir === 2){
            nx ++;
        }else if(dir === 3){
            ny --;
        }
    }
    return cnt;
}

function getAnswer(copy){
    let dp = Array.from({length:n},()=>Array.from({length:m},()=>0));
    let cnt = 0;
    for(let [x,y,type,dir] of copy){
        cnt += checking(dp,x,y,dir);
        if(type === 2){
            // 반대편
            cnt += checking(dp,x,y,(dir + 2) % 4);
        }
        if(type === 3){
            // 오른쪽편
            cnt += checking(dp,x,y,(dir+1) % 4);
            
        }
        if(type >= 4){
            cnt += checking(dp,x,y,(dir+1) % 4);
            cnt += checking(dp,x,y,(dir + 2) % 4);
        }
        if(type === 5){
            cnt += checking(dp,x,y,(dir + 3) % 4);
        }
    }
    answer = Math.max(cnt, answer)
}

function dfs(idx, copy){
    if(idx === camera.length){
        getAnswer(copy);
        return;
    }
    const [x,y] = camera[idx];
    const type = arr[x][y];
    for(let i =0 ; i <4; i++){
        dfs(idx+1,  [...copy, [x,y,type,i]])
    }
    // // copy.push([x,y,type,dir]);
    // dfs(idx + 1, 0, [...copy,[x,y,type,dir]])
    // dfs(idx + 1, 1, [...copy,[x,y,type,dir]])
    // dfs(idx + 1, 2, [...copy,[x,y,type,dir]])
    // dfs(idx + 1, 3, [...copy,[x,y,type,dir]])
    
}









