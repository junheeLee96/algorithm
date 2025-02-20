const readline = require('readline');

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout,
})

class Heap{
    constructor(){
        this.heap = []
    }
    getParent(idx){
        return Math.floor((idx - 1) / 2)
    }
    getLeft(idx){
        return 2 * idx + 1
    }
    getRight(idx){
        return 2 * idx + 2
    }
    swap(i,j){
        [this.heap[i],this.heap[j]]= [this.heap[j],this.heap[i]]
    }
    up(){
        let index = this.heap.length - 1;
        while( index > 0 ){
            let parent = this.getParent(index);
            if(this.heap[parent][0] < this.heap[index][0]) break;

            this.swap(index, parent)
            index = parent;
        }
    }
    down(index = 0){
        const length = this.heap.length;

        while(this.getLeft(index) < length){
            let left = this.getLeft(index);
            let right = this.getRight(index);

            if(right < length && this.heap[right][0] < this.heap[left][0]){
                left = right;
            }
            if(this.heap[index][0] <= this.heap[left][0]) break;

            this.swap(left,index);
            index = left
        }
    }
    pop(){
        if(this.heap.length === 0) return null
        if(this.heap.length === 1) return this.heap.pop();
        const min = this.heap[0];
        this.heap[0] = this.heap.pop()
        this.down();
        return min;
    }
    push(num){
        this.heap.push(num);
        this.up();
    }
}

let n,e;
let arr ;
let start,end;
let temp = 0;

const INF = Infinity;
let end1,end2

rl.on('line',(line)=>{
    if(!n){
        [n,e] = line.split(' ').map(Number);
        arr = Array.from({length:n+1},()=>[])
    }else if (temp < e){
        const [a,b,c] = line.split(' ').map(Number);
        arr[a].push([b,c])
        arr[b].push([a,c])
        temp ++;
    }else{
        [end1,end2] =  line.split(' ').map(Number);
    }
    
}).on('close',()=>{
    const to_end = dj(1);
    const end1_to_n=dj(end1)
    const end2_to_n=dj(end2);
    let answer = Math.min(to_end[end1] + end1_to_n[end2] + end2_to_n[n], to_end[end2] + end2_to_n[end1]+ end1_to_n[n]);
    console.log(answer >= INF ? -1 : answer);
    
})

function dj(start){
    const distance = Array.from({length:n+1},()=>INF);
    distance[start] = 0;
    let q = new Heap();
    q.push([0, start]);

    while(q.heap.length > 0){
        let [dist,now ] = q.pop();

        if(distance[now] < dist) continue;

        for(let[nxt,cost] of arr[now]){
            const newCost = cost + dist;
            if(distance[nxt] > newCost){
                distance[nxt] = newCost;
                q.push([newCost,nxt])
            }
        }
    }
    return distance
}