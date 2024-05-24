class MinHeap {
    constructor() {
        this.heap = [];
    }

    // 부모 노드 인덱스 계산
    getParentIndex(index) {
        return Math.floor((index - 1) / 2);
    }

    // 왼쪽 자식 노드 인덱스 계산
    getLeftChildIndex(index) {
        return 2 * index + 1;
    }

    // 오른쪽 자식 노드 인덱스 계산
    getRightChildIndex(index) {
        return 2 * index + 2;
    }

    // 힙에 값 추가
    insert(value) {
        this.heap.push(value);
        this.heapifyUp();
    }

    // 루트 노드 제거
    remove() {
        if (this.heap.length === 0) {
            return null;
        }
        if (this.heap.length === 1) {
            return this.heap.pop();
        }
        const root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return root;
    }

    // 위로 힙 정렬 (Heapify Up)
    heapifyUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            const parentIndex = this.getParentIndex(index);
            if (this.heap[parentIndex] > this.heap[index]) {
                [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    // 아래로 힙 정렬 (Heapify Down)
    heapifyDown() {
        let index = 0;
        const length = this.heap.length;
        while (this.getLeftChildIndex(index) < length) {
            let smallestChildIndex = this.getLeftChildIndex(index);
            const rightChildIndex = this.getRightChildIndex(index);

            if (rightChildIndex < length && this.heap[rightChildIndex] < this.heap[smallestChildIndex]) {
                smallestChildIndex = rightChildIndex;
            }

            if (this.heap[index] > this.heap[smallestChildIndex]) {
                [this.heap[index], this.heap[smallestChildIndex]] = [this.heap[smallestChildIndex], this.heap[index]];
                index = smallestChildIndex;
            } else {
                break;
            }
        }
    }

    // 힙의 최소값 확인
    peek() {
        return this.heap.length === 0 ? null : this.heap[0];
    }

    // 힙의 크기 확인
    size() {
        return this.heap.length;
    }
}

function solution(scoville, K) {
    let answer = 0;
    const minHeap = new MinHeap();
    scoville.forEach((e) => minHeap.insert(e));
    
    while(minHeap.peek() < K) {
        if (minHeap.size() === 1) return -1;
        
        const a = minHeap.remove();
        const b = minHeap.remove();
        
        minHeap.insert(a + b * 2);
        answer += 1;
    }
    return answer;
}