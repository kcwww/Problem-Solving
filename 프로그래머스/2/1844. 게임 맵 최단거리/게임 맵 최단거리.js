function solution(maps) {
    let answer = 0;
    const row = maps.length;
    const col = maps[0].length;
    const queue = [[0,0,0]];
    const move = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    maps[0][0] = 0;
    while (queue.length !== 0) {
        const [r, c, cnt] = queue.shift();

        if (r === row - 1 && c === col - 1) {answer = cnt; break;}
        
        for (let i = 0; i < 4; i++) {
            const nr = move[i][0] + r;
            const nc = move[i][1] + c;

            if (nr >= 0 && nr < row && nc >= 0 && nc < col && maps[nr][nc] === 1) {
                maps[nr][nc] = 0;
                queue.push([nr, nc, cnt + 1]);
            }
        }
    }
    if (answer === 0) answer = -2;
    return answer + 1;
}