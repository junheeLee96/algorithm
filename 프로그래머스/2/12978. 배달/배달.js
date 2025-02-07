class Heap{
    constructor(){
        this.heap = []
    }
    getParent(idx){
        return Math.floor((idx - 1) / 2 )
    }
    getLeft(idx){
        return 2 * idx + 1
    }
    getRight(idx){
        return 2 * idx + 2;
    }
    swap(i,j){
        [this.heap[i] , this.heap[j] ] = [this.heap[j] , this.heap[i] ]
    }
    
    up(){
        let index = this.heap.length - 1;
        
        while (index > 0){
            let parent = this.getParent(index);
            
            if(this.heap[parent][0] < this.heap[index][0] ) break;
            this.swap(parent,index);
            index = parent;
        }
    }
    down(index = 0){
        let length = this.heap.length;
        
        while(this.getLeft(index) < length){
            let left = this.getLeft(index);
            let right = this.getRight(index);
            
            if(right < length && this.heap[left][0] > this.heap[right][0]){
                left = right
            }
            if(this.heap[left][0] >= this.heap[index][0]) break;
            this.swap(left,index);
            index = left;
        }
    }
    push(n){
        this.heap.push(n)
        this.up()
    }
    pop(){
        if(this.heap.length === 0) return null;
        if(this.heap.length === 1) return this.heap.pop();
        
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.down()
        return min
    }
}

function solution(N, road, K) {
    var answer = 0;

    let q = new Heap();
    const arr = Array.from({length:N+1},()=>[]);
    
    for(let d of road){
        let [a,b,c] = d;
        arr[b].push([a,c]);
        arr[a].push([b,c])
    }
    
    function dj(start){
        const q= new Heap();
        q.push([0,start]);
        
        const distance = Array.from({length:N+1} ,()=>Infinity);
        distance[start] = 0;
        
        while (q.heap.length > 0){
            const [dist,now ] = q.pop();
            
            if(distance[now] < dist) continue;
            
            for(let [nxt,cost] of arr[now]){
                const newCost = cost + dist;
                
                if(distance[nxt] > newCost){
                    q.push([newCost,nxt]);
                    distance[nxt] = newCost
                }
            }
        }
        return distance
    }
    
    const distance= dj(1)
    return distance.filter(d => d <= K).length;

}