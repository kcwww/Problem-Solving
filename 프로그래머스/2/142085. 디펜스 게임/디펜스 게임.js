class PriorityQueue {
    constructor(comparator = (a, b) => a - b) {
        this._heap = [];
        this._comparator = comparator;
    }

    size() {
        return this._heap.length;
    }

    isEmpty() {
        return this.size() === 0;
    }

    push(value) {
        this._heap.push(value);
        this._siftUp();
    }

    pop() {
        const poppedValue = this._heap[0];
        const bottom = this.size() - 1;
        if (bottom > 0) {
            this._swap(0, bottom);
        }
        this._heap.pop();
        this._siftDown();
        return poppedValue;
    }

    peek() {
        return this._heap[0];
    }

    _parent(idx) {
        return Math.floor((idx - 1) / 2);
    }

    _leftChild(idx) {
        return idx * 2 + 1;
    }

    _rightChild(idx) {
        return idx * 2 + 2;
    }

    _compare(i, j) {
        return this._comparator(this._heap[i], this._heap[j]);
    }

    _swap(i, j) {
        [this._heap[i], this._heap[j]] = [this._heap[j], this._heap[i]];
    }

    _siftUp() {
        let nodeIdx = this.size() - 1;
        while (nodeIdx > 0 && this._compare(nodeIdx, this._parent(nodeIdx)) < 0) {
            this._swap(nodeIdx, this._parent(nodeIdx));
            nodeIdx = this._parent(nodeIdx);
        }
    }

    _siftDown() {
        let nodeIdx = 0;
        while (
            (this._leftChild(nodeIdx) < this.size() && this._compare(this._leftChild(nodeIdx), nodeIdx) < 0) ||
            (this._rightChild(nodeIdx) < this.size() && this._compare(this._rightChild(nodeIdx), nodeIdx) < 0)
        ) {
            const minChildIdx =
                this._rightChild(nodeIdx) < this.size() &&
                this._compare(this._rightChild(nodeIdx), this._leftChild(nodeIdx)) < 0
                    ? this._rightChild(nodeIdx)
                    : this._leftChild(nodeIdx);
            this._swap(nodeIdx, minChildIdx);
            nodeIdx = minChildIdx;
        }
    }
}

const solution = (n, k, enemy) => {
    const len = enemy.length;
    let answer = k >= len ? len : k;

    const queue = new PriorityQueue(); // 우선순위 큐 사용

    // 초기 큐 설정
    for (let i = 0; i < k; i++) {
        queue.push(enemy[i]);
    }

    for (let i = k; i < len; i++) {
        const num = enemy[i];
        if (queue.peek() < num) {
            const left = queue.pop();
            queue.push(num);
            n -= left;
        } else n -= num;

        if (n >= 0) answer += 1;
        if (n <= 0) break;
    }

    return answer;
};
