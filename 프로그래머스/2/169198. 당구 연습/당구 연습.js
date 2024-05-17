function checkMinimum(x,y, bx, by, m, n) {
    const symmetry = [[bx, by + 2 * (n - by)], [bx, -by], [bx + 2 * (m - bx), by], [-bx, by]];
    const gradient = [bx - x, by - y];
    if (gradient[0] === 0) {
        if (gradient[1] > 0) symmetry[0] = null;
        else symmetry[1] = null;
    } else if (gradient[1] === 0) {
        if (gradient[0] > 0) symmetry[2] = null;
        else symmetry[3] = null;
    }
    let min = -1;
    symmetry.forEach((e) => {
        if (e === null) return;
        const result = Math.pow(e[0] - x, 2) + Math.pow(e[1] - y, 2);
        min = min === -1 ? result : (min > result ? result : min);
    })
    return min;
}

function solution(m, n, startX, startY, balls) {
    // 리스트에 맞는 순서대로 공을 맞춰야함
    // 원쿠션시에 공이 굴러간 거리의 최소값 의 제곱 구하기
    // 대칭이동, 선 대칭일 경우 제외
    
    //선 대칭일 경우 기울기 0 확인
    let answer = [];
    
    balls.forEach((e) => {
        const min = checkMinimum(startX, startY, e[0], e[1], m, n);
        answer.push(min);
    });
    return answer;
}