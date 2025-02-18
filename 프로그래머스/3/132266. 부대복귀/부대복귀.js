class Heap{
    constructor(){
        this.heap = [];
    }
    getParent (idx){
        return Math.floor((idx - 1) / 2);
    }
    getLeft (idx){
        return 2 * idx + 1
    }
    getRight(idx){
        return 2 * idx + 2
    }
    swap(x,y){
        [this.heap[x],this.heap[y]] = [this.heap[y],this.heap[x]]
    }
    up(){
        let index = this.heap.length - 1;
        while(index > 0){
            let parent = this.getParent(index);
            
            if(this.heap[parent][0] < this.heap[index][0]) break;
            this.swap(parent,index);
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
            if(this.heap[left][0] >= this.heap[index][0]) break;
            this.swap(left,index);
            index = left;
        }
    }
    pop(){
        if(this.heap.length === 0) return null;
        if(this.heap.length === 1) return this.heap.pop();
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.down();
        return min
    }
    push(n){
        this.heap.push(n);
        this.up();
    }
}

const INF = Infinity;
let arr = [];

function solution(n, roads, sources, destination) {
    var answer = [];
    arr = Array.from({length:n+1},()=>[]);
    for(let [a,b] of roads){
        arr[a].push([b,1]);
        arr[b].push([a,1]);
    }
    
    const distance = dj(destination,n);
    for(let s of sources){
        answer.push(distance[s] === INF ? -1 : distance[s])
    }
    return answer;
}

function dj(start,n){
    let q = new Heap();
    q.push([0,start]);
    const distance = Array.from({length:n+1},()=>INF);
    distance[start] = 0;
    
    while (q.heap.length > 0){
        const [dist, now] = q.pop();
        
        if(distance[now] < dist) continue;
        
        for(let [nxt,cost] of arr[now]){
            const newCost = cost + dist;
            if(distance[nxt] > newCost){
                distance[nxt] = newCost;
                q.push([newCost,nxt]);
            }
        }
    }
    return distance
}