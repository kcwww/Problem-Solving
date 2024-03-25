function solution(picks, minerals) {
    // 곡괭이 0~5
    // 피로도 누적
    // 공괭이는 종류 상관없이 5개 캐면 중지
    // 곡괭이 선택- > 다써야함 -> 순서대로만 캘수 있음 광물 -> 모두 캐거나 곡괭이  없을떄까지
    // 최소한의 피로도 리턴
    let answer = 0;
    
    // 곡괭이 갯수로 캘수 있는 광물 자르자
    // 광물 5개씩 피로도 계산
    // 피로도 별로 곡괭이 정렬
    
    
    let mining = picks.reduce((ac, cu) => {
        return (ac + cu);
    }, 0);
    
    const sliceArr = [];
    
    for (let i = 0; i < mining; i++) {
        const arr = minerals.splice(0, 5);
        if (arr.length === 0) break;
        sliceArr.push(arr);
    }
    
    const fatigue = [];
    sliceArr.forEach((element) => {
        const fati = [0,0,0];
        element.forEach((e) => {
            if (e === "diamond") {
                fati[1] += 5;
                fati[2] += 25;
            }
            else if (e === "iron") {
                fati[1] += 1;
                fati[2] += 5;
            } else {
                fati[1] += 1;
                fati[2] += 1;
            }
            fati[0] += 1;
        });
        fatigue.push(fati);
    });
    
    
    fatigue.sort((a,b) => {
        if (a[2] === b[2] && a[1] === b[1]) return b[0] - a[0];
        else if (a[2] === b[2]) return b[1] - a[1];
        return b[2] - a[2];
    })
    
    
    fatigue.forEach((element) => {
        if (picks[0] > 0) {
            picks[0] -= 1;
            answer += element[0];
        } else if (picks[1] > 0) {
            picks[1] -= 1;
            answer += element[1];
        } else if (picks[2] > 0) {
            picks[2] -= 1;
            answer += element[2];
        }
    })
    return answer;
}