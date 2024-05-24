function solution(line) {
    const answer = [];
    const length = line.length;
    
    for (let i = 0; i < length; i++) {
        for (let j = i + 1; j < length; j++) {
            const [a1, b1, c1] = line[i].map(v => +v);
            const [a2, b2, c2] = line[j].map(v => +v);
            const denominator = a1 * b2 - a2 * b1;

            // 평행한 직선 처리
            if (denominator === 0) continue;
            
            const x = (b1 * c2 - b2 * c1) / denominator;
            const y = (a2 * c1 - a1 * c2) / denominator;
            
            if (Number.isInteger(x) && Number.isInteger(y)) {
                answer.push([x, y]);
            }
        }
    }
    
    // 교점이 없는 경우 처리
    if (answer.length === 0) return [];

    let [minX, maxX] = [Infinity, -Infinity];
    let [minY, maxY] = [Infinity, -Infinity];
    answer.forEach(([x, y]) => {
        if (minX > x) minX = x;
        if (maxX < x) maxX = x;
        if (minY > y) minY = y;
        if (maxY < y) maxY = y;
    });

    const result = [];
    for (let i = 0; i <= maxY - minY; i++) {
        result.push(new Array(maxX - minX + 1).fill('.'));
    }
    
    answer.forEach(([x, y]) => {
        const row = maxY - y;
        const col = x - minX;
        result[row][col] = '*';
    });
    
    return result.map(row => row.join(''));
}
