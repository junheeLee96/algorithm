class Heap {
    constructor() {
        this.heap = [];
    }

    getParent(idx) {
        return Math.floor((idx - 1) / 2);
    }

    getLeft(idx) {
        return 2 * idx + 1;
    }

    getRight(idx) {
        return 2 * idx + 2;
    }

    swap(x, y) {
        [this.heap[x], this.heap[y]] = [this.heap[y], this.heap[x]];
    }

    up() {
        let index = this.heap.length - 1;
        while (index > 0) {
            let parent = this.getParent(index);
            if (this.heap[parent] < this.heap[index]) break;
            this.swap(parent, index);
            index = parent;
        }
    }

    down(index = 0) {
        const length = this.heap.length;
        while (this.getLeft(index) < length) {
            let left = this.getLeft(index);
            let right = this.getRight(index);
            if (right < length && this.heap[left] > this.heap[right]) {
                left = right;
            }
            if (this.heap[index] < this.heap[left]) break;
            this.swap(left, index);
            index = left;
        }
    }

    pop() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.down();
        return min;
    }

    push(num) {
        this.heap.push(num);
        this.up();
    }

    remove(num) {
        const index = this.heap.indexOf(num);
        if (index === -1) return;

        this.heap.splice(index, 1);
        this.down(index);
    }
}

function solution(operations) {
    let q = new Heap();
    let rq = new Heap()

    for (let o of operations) {
        let [a, b] = o.split(' ');
        b = parseInt(b);

        if (a === 'I') {
            q.push(b);
            rq.push(-b)
        }

        if (a === 'D' && b === 1) {
            const num = rq.pop();
            if(!num) continue;
            q.remove(-num)
        }

        if (a === 'D' && b === -1) {
            const num = q.pop();
            if(!num) continue;
            rq.remove(-num)
        }
    }

    if (q.heap.length === 0) {
        return [0, 0];
    }
    const max = rq.pop();
    const min = q.pop();
    return [-max, min];
}
