function solution(storage, requests) {
    var answer = 0;
    let n = storage.length;
    let m = storage[0].length
    let arr = Array.from({length:1},()=>Array.from({length:m+2},()=>''));
    for(let i =0; i < storage.length; i ++){
        let a = ['', ...storage[i], ''];
        arr.push(a)
    }
    arr.push(Array.from({length:m+2},()=>''));

    for(let str of requests){
        bfs(arr,str,n+2,m+2)
    }

    for(let a of arr){
        answer += a.filter(v => v !== '').length;
    }
    return answer;
}

const dx = [0,0,-1,1];
const dy = [-1,1,0,0]

function bfs(arr,str,n,m){
    let visit = Array.from({length:n},()=>Array.from({length:m},()=>false));
    visit[0][0] = true
    let q= [[0,0]];

    let his = {}

    while(q.length > 0){
        const [x,y] = q.pop();

        for(let i=0; i < 4; i++){
            const nx = x + dx[i];
            const ny = y + dy[i];

            if(0 <= nx && nx < n && 0 <= ny && ny < m && visit[nx][ny] === false){
                if(str[0] === arr[nx][ny]){
                    his[`${nx} ${ny}`] = 1
                    // his.set(`${nx} ${ny}`,1)
                }
                if(str.length === 1 && arr[nx][ny] === ''){
                    visit[nx][ny] = true;
                    q.push([nx,ny])
                }else if(str.length === 2){
                    visit[nx][ny] = true;
                    q.push([nx,ny])
                }
            }
        }
    }
    for(let key in his){
        const [x,y] = key.split(' ').map(Number);
        arr[x][y] = ''
    }
}