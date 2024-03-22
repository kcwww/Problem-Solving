function findRandomNode (outNode, onlyOut) {
    while (onlyOut.length) {
        const num = onlyOut.pop();
        
        if (outNode[num].length > 1) return num;
    }
}

function checkEight(node, start, result, visit) {
    const queue = [...node[start]];
    result[3] += 1;
    

    
    while (queue.length) {
        const num = queue.shift();
        
        if (visit[num]) continue; // 방문처리
        if (num === start) continue; // 원점 처리
        visit[num] = true;
        queue.push(...node[num]);
        
    }
    
}

function checkGraph(node, result) {

    // 막대, 본인에서 다른곳 방향은 항상 하나
    // 도넛, 본인에서 본인, 방향은 항상 하나
    // 8자 모양, 본인에서 본인, 방향은 여러개
    
    // 8자 : 시작 넘버 -> 순환하다 방향이 2개 -> 8자 시작
    // 도넛 : 시작 넘버 -> 순환 -> 모든큐 소진 -> 자기 자신으로 돌아오는지 확인
    // 막대 : 순환 -> 마지막 0값 체크
    
    const visit = {};
    const stick = {};
    
    for (let key in node) {
        if (visit[key]) continue;
    
        const start = +key;
        visit[start] = true;
        
        let temp = node[start][0];
        
        if (start === temp) {
            result[1] += 1;
            continue; // 도넛 1개
        }
        
        if (temp === 0) {
            result[2] += 1;
            stick[start] = true;
            continue ; // 막대 마지막 노드 1개
        }
        
        
        let stack = [temp];
        
        if (node[start].length > 1) {
            checkEight(node, start, result, visit);
            continue;
        }
        

        
        while (start !== temp) {
            
            //8자 체크
            if (node[temp].length > 1) {
                checkEight(node, start, result, visit);
                stack = [];
                break;
            }
            
            const newTemp = node[temp][0];
            
            
            // 막대 체크
            if (newTemp === 0 && stick[temp] === undefined) {
                stick[temp] = true;
                result[2] += 1;
                break;
            } else if (newTemp === 0 && stick[temp]) {
                break;
            }
            
            // 도넛 체크
            if (newTemp === start) {
                result[1] += 1;
            }
            temp = newTemp;
            stack.push(temp);
        }
        
        stack.forEach((e) => {
            visit[e] = true;
        })
            
        }
}





function solution(edges) {
    // random node 를 찾아서 지우자
    // random node 와 막대 그래프 차이 구분
    
    // 나가는 간선만 있는 노드 찾고
    // 들어오기만 하는 노드 찾고
    // 해당 노드로 가며 사이즈 체크
    
    // 랜덤 노드 지우고 나머지 판단
    // 도넛은 자기 자신으로 돌아오고 사이즈가 이동 횟수
    // 막대는 자기자신으로 돌아오지 않음 사이즈도 이동 횟수
    // 8자 모양은 자기자신으로 돌아옴 하지만 여러 방문이 있을수 있어 bfs
    
    
    var answer = [];
    
    
    const outNode = {};
    const inNode = {};
    
    
    edges.forEach((e) => {
        if (outNode[e[0]] === undefined) outNode[e[0]] = [e[1]];
        else outNode[e[0]].push(e[1]);
        
        if (inNode[e[1]] === undefined) inNode[e[1]] = [e[0]];
        else inNode[[e[1]]].push(e[0]);
    })
    
    const onlyOut = [];
    for (let key in outNode) {
        if (inNode[key] === undefined) onlyOut.push(+key);
    }
    
    const randomNode = findRandomNode(outNode, onlyOut);
    delete outNode[randomNode];
    const result = [randomNode,0,0,0];
    
    for (let key in inNode) {
        if (outNode[key] === undefined) outNode[key] = [0];
    }
    
    checkGraph(outNode, result);
    return result;
}


