class Heap{
    heap = []
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
        [this.heap[i],this.heap[j]] = [this.heap[j],this.heap[i]]
    }
    up(){
        let index = this.heap.length - 1;
        while(index > 0){
            let parent = this.getParent(index);
            if(this.heap[parent] <= this.heap[index]) break;
            
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
            if(this.heap[left] > this.heap[index]) break;
            
            this.swap(left,index);
            index = left
        }
    }
    pop(){
        if(this.heap.length === 1) return this.heap.pop();
        if(this.heap.length === 0) return null;
        
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.down();
        return min;
    }
    push(n){
        this.heap.push(n);
        this.up();
    }
}

function solution(book_time) {
    var answer = 0;
    
    
    for(let i =0; i < book_time.length; i ++){
        let [start,end] = book_time[i];
        start = start.split(':').map(Number);
        start = start[0] * 60 + start[1];
        end = end.split(':').map(Number);
        end = end[0] * 60 + end[1];
        book_time[i] = [start,end]
    }
    book_time.sort((a,b)=> {
        if(a[0] === b[0]){
            return a[1] - b[1]
        }
        return a[0] - b[0]
    })
    console.log(book_time)
    let q= new Heap()
    q.push(book_time[0][1] + 10);
    let cnt = 1;
    for(let i = 1; i < book_time.length; i ++){
        const [start,end] = book_time[i];
        const room = q.pop();
        if(start < room){
            q.push(room);
            q.push(end + 10);
        }else{
            q.push(end + 10)
        }
    }
    return q.heap.length;
}