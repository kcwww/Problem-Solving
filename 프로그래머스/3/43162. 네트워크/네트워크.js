function dfs(computers, i, visited) {
    if (visited[i] === 1) return;
    const computer = computers[i];
    
    visited[i] = 1;
    
    computer.forEach((e, index) => {
        if (index === i) return;
        
        if (e === 1) dfs(computers, index, visited)
    })
    return ;
}

function solution(n, computers) {
    // dfs
    // 모든 노드 방문 처리 && 갯수 세기
    
    let answer = 0;
    const visited = new Array(n).fill(0);
    
    for (let i = 0; i < n; i++) {
        if (visited[i] === 1) continue;
        
        answer += 1;
        
        dfs(computers, i, visited);
    }
    
    return answer;
}