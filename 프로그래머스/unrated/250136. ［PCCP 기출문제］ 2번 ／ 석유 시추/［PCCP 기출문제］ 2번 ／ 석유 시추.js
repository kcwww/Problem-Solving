function bfs(visited, k, i, idx, row, col) {
    let move = [[1,0], [-1,0], [0,1], [0,-1]];
    let oil = 0;
    let queue = [[k, i]];
    
    while (queue.length !== 0) {
        let [x,y] = queue.shift()
        if (visited[x][y] !== 1)
            continue;
        oil += 1;
        visited[x][y] = idx;
        
        for (let i = 0; i < 4; i++) {
            let nx = x + move[i][0];
            let ny = y + move[i][1];
            if (nx >= 0 && nx < row && ny >= 0 && ny < col) {
                if (visited[nx][ny] === 1)
                    queue.push([nx,ny])
            }
        }
    }
    return oil;
}

function getOil(i, land, row, col, cluster, column) {
    let oil = 0;
    const oilSum = {};

    for (let k = 0; k < land.length; k++) {
        if (land[k][i] === 1) {
            oil = bfs(land, k, i, column.idx, row, col);
            if (cluster[column.idx] === undefined) {
                cluster[column.idx] = oil;
                oilSum[column.idx] = oil;
                column.idx -= 1;
            }
        } else if (land[k][i] !== 1 && land[k][i] !== 0) {
            const cidx = land[k][i];
            oilSum[cidx] = cluster[cidx];
        }
    }
    return oilSum;
}


function solution(land) {
    // 열에 따라 시추관
    // 가장 많은 석유량 리턴
    let oil = 0;
    
    const column = {
        idx : -1
    };
    const cluster = {};
    const row = land.length;
    const col = land[0].length;
    
    for (let i = 0; i < land[0].length; i++) {
        const oilSum = getOil(i, land, row, col, cluster, column);
        column[i] = oilSum;
    }
    delete column['idx'];
    
    for (const key in column) {
  let value = 0;
  for (const key2 in column[key]) {
    value += column[key][key2];
  }
  if (value > oil) {
    oil = value;
  }
}
    
    return oil;
}