let info = {};
let INF = Infinity;
let dist;

function solution(n, s, a, b, fares) {
    info = { n, s, a, b };

    // 최단 거리 배열 초기화
    dist = Array.from({ length: n + 1 }, () =>
        Array.from({ length: n + 1 }, () => INF)
    );

    // 자기 자신으로 가는 비용 0으로 설정
    for (let i = 1; i <= n; i++) {
        dist[i][i] = 0;
    }

    // 주어진 간선 정보를 dist 배열에 반영
    for (let [u, v, cost] of fares) {
        dist[u][v] = cost;
        dist[v][u] = cost;
    }

    // 플로이드 와샬 알고리즘 실행
    floyd(n);

    
    var answer = INF;
    for(let i =1; i <=n; i ++){
       const to_a = dist[i][a]
       const to_b = dist[i][b];
        const from_s = dist[i][s];
        answer = Math.min(answer, to_a + to_b + from_s)
    }
    return answer;
}

function floyd(n) {
    for (let k = 1; k <= n; k++) {
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                if (
                    dist[i][k] !== INF &&
                    dist[k][j] !== INF &&
                    dist[i][j] > dist[i][k] + dist[k][j]
                ) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}



// class Heap{
//     constructor(){
//         this.heap = []
//     }
//     getParent (idx){
//         return Math.floor((idx - 1) / 2)
//     }
//     getLeft(idx){
//         return 2 * idx + 1
//     }
//     getRight (idx){
//         return 2 * idx + 2
//     }
//     swap(q,w){
//         [this.heap[q],this.heap[w]] =[this.heap[w],this.heap[q]] 
//     }
//     up(){
//         let index = this.heap.length - 1;
        
//         while(index > 0){
//             let parent = this.getParent(index);
            
//             if(this.heap[parent][0] < this.heap[index][0]) break;
//             this.swap(parent,index);
//             index = parent;
//         }
//     }
//     down(index = 0){
//         const length = this.heap.length;
        
//         while(this.getLeft(index) < length){
//             let left = this.getLeft(index);
//             let right = this.getRight(index);
            
//             if(right < length && this.heap[left][0] > this.heap[right][0]){
//                 left = right
//             }
//             if(this.heap[left][0] >= this.heap[index][0]) break;
            
//             this.swap(left,index);
//             index = left
//         }
//     }
//     pop(){
//         if(this.heap.length=== 0) return null;
//         if(this.heap.length === 1) return this.heap.pop();
        
//         const min = this.heap[0];
//         this.heap[0] = this.heap.pop();
//         this.down();
//         return min;
//     }
//     push(num){
//         this.heap.push(num)
//         this.up();
//     }
// }

// let arr ;
// let info;
// let direct = {
//     a:0,b:0,
// }


// function solution(n, s, a, b, fares) {
//     var answer = Infinity;
//     info ={
//         n,s,a,b
//     }
//     arr = Array.from({length:n+1},()=>[]);
    
//     for(let [a,b,c] of fares){
//         arr[a].push([b,c])
//         arr[b].push([a,c]);
//     }
//     for(let i = 1; i <n+1; i++){
//         let money = 0;
//         if(i === s) continue
//         if(i === a){
//             money = dj(a);
//         }else if(i === b){
//             money = dj(b);
//         }else{
//             money = dj(i)
//         }
//         answer = Math.min(money,answer)
//     }
//     return Math.min(answer , direct.a + direct.b);
// }

// function dj(mid){
//     let {s,a,b} = info;
//     let start_to_mid = daji(s,mid);
//     let mid_to_a = daji(mid,a)
//     let mid_to_b = daji(mid,b);
    
//     if(mid === a){
//         direct.a = start_to_mid
//     }
//     if(mid === b){
//         direct.b = start_to_mid
//     }
    
//     return start_to_mid + mid_to_a + mid_to_b
// }

// function daji(start,end){
//     let {n} = info
//     let distance = Array.from({length:n+1},()=>Infinity);
//     distance[start] = 0;
//     let q = new Heap();
    
//     q.push([0,start]);
    
//     while(q.heap.length > 0){
//         let [dist, now] = q.pop();
//         if(distance[now] < dist) continue;
        
//         for(let [nxt,cost] of arr[now]){
//             const newCost = cost + dist;
            
//             if(distance[nxt] > newCost){
//                 distance[nxt] = newCost;
//                 q.push([newCost,nxt])
//             }
//         }
//     }
    
//     return distance[end] 
// }