function solution(points, routes) {
    // 로봇마다 배열 생성
    // 로봇들 배열 순회하며 중복 검사
    let answer = 0;
    const robots = [];
    const robotCnt = routes.length;
    
    for (const route of routes) {
        const robot = [];
        const start = [...points[route[0] - 1]];

        robot.push([...start]);
        
        for (let i = 1; i < route.length; i++) {
            const to = points[route[i] - 1];
            let r = to[0] - start[0];
            let c = to[1] - start[1];
 
            
            while (r !== 0) {
                if (r > 0) {
                    start[0] += 1;
                    r -= 1;
                } else if (r < 0) {
                    start[0] -= 1;
                    r += 1;
                }
                robot.push([...start]);
            }
            
            while (c !== 0) {
                if (c > 0) {
                    start[1] += 1;
                    c -= 1;
                } else if (c < 0) {
                    start[1] -= 1;
                    c += 1;
                }
                robot.push([...start]);
            }
        }
        robots.push(robot);
    }
    
    
    let time = 0;
    while (true) {
        let flag = true;
        const countMap = {};
        for (let i = 0; i < robotCnt; i++) {
            if (time >= robots[i].length) continue;
            flag = false;
            const key = JSON.stringify(robots[i][time]);
            countMap[key] = (countMap[key] || 0) + 1;
        }
        
        if (flag) break;
        
        for (const key in countMap) {
            if (countMap[key] > 1) {
                answer += 1;
            }
        }
        time += 1;
    }
    
    return answer;
}