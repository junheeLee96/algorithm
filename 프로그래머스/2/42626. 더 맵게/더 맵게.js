class Heap{
    constructor(){
        this.heap = [];
    }
    getParent (idx){
        return Math.floor((idx - 1) / 2);
    }
    getLeft(idx){
        return 2 * idx + 1;
    }
    getRight (idx){
        return 2 * idx + 2
    }
    swap(x,y){
        [this.heap[x],this.heap[y]] = [this.heap[y],this.heap[x]];
    }
    up(){
        let index = this.heap.length - 1;
        while(index > 0){
            let parent = this.getParent(index);
            if(this.heap[parent] < this.heap[index]) break;
            this.swap(parent,index);
            index = parent;
        }
    }
    down(index = 0){
        const length = this.heap.length;
        
        while(this.getLeft(index) < length){
            let left = this.getLeft(index);
            let right = this.getRight(index);
            
            if(right < length && this.heap[left] > this.heap[right]){
                left = right;
            }
            if(this.heap[left] >= this.heap[index]) break;
            this.swap(left,index);
            index = left;
        }
    }
    pop(){
        if(this.heap.length === 1) return this.heap.pop();
        if(this.heap.length === 0) return null
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.down();
        return min
    }
    push(n){
        this.heap.push(n);
        this.up();
    }
    check(){
        return this.heap[0]
    }
}

function solution(scoville, K) {
    let k = K
    var answer = 0;
    let q = new Heap();
    for(let n of scoville){
        q.push(n)
    }
    let cnt = 0;
    while(q.check() < k){
        cnt ++;
        if(q.heap.length < 2){
            cnt = -1
            break
        }
        let m1 = q.pop();
        let m2 = q.pop();
        let num = m1 + (m2 * 2);
        q.push(num)
    }
    return cnt;
}