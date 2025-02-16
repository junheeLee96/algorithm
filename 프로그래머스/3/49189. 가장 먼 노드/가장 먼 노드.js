class Heap{
    heap = []
    getParent(idx){
        return Math.floor((idx - 1) / 2);
    }
    getLeft(idx){
        return 2 * idx + 1;
    }
    getRight(idx){
        return 2 * idx + 2;
    }
    swap(x,y){
        [this.heap[x],this.heap[y]] = [this.heap[y],this.heap[x]]
    }
    up(){
        let index = this.heap.length - 1;
        while (index > 0){
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
            
            if(right < length && this.heap[left][0] > this.heap[right][0]){
                left = right
            }
            if(this.heap[left][0] > this.heap[index][0]) break;
            
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
        return min;
    }
    push(num){
        this.heap.push(num);
        this.up()
    }
}

const INF = Infinity
function solution(n, vertex) {
    
    let distance = Array.from({length:n+1},()=>INF);
    const arr  = Array.from({length:n+1},()=>[]);
    
    for(let [a,b] of vertex){
        arr[a].push([b,1])
        arr[b].push([a,1])
    }
    dj(distance,1,arr)
     distance.splice(0,1)
    distance.sort((a,b)=> b-a);
    const mx = distance[0]
    return (distance.filter(v=> v===mx).length)
}

function dj(distance,start,arr){
    let q = new Heap();
    distance[start] = 0;
    q.push([0,start])
    
    while(q.heap.length > 0){
        let [dist,now] = q.pop();
        
        if(distance[now] < dist){
            continue;
        }
        
        for(let [nxt, cost] of arr[now]){
            let newCost = cost + dist;
            if(newCost < distance[nxt]){
                distance[nxt] = newCost;
                q.push([newCost,nxt]);
            }
        }
    }
    
}