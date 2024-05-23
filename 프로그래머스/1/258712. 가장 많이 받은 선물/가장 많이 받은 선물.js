function solution(friends, gifts) {
    // 두 사람이 선물을 주고 받은 기록 -> 더 많은 선물을 준 사람이 받음
    
    // 두 사람이 선물을 주고 받은 기록 X or 같 -> 선물 지수가 더 큰 사람이 작은 사람에게 하나 받
    // 선물 지수 = 준 선물의 수 - 받은 선물의 수
    // 선물 지수도 같으면 주고받지않음
    
    // gift a -> b
    
    const name = {};
    const next = {};
    const giftScore = {};
    
    friends.forEach((v) => {
        name[v] = {};
        next[v] = 0;
        giftScore[v] = 0;
    })
    
    
    gifts.forEach((e) => {
        const [a, b] = e.split(" ");
        if (name[a][b] === undefined) name[a][b] = 0;
        name[a][b] += 1;
        giftScore[a] += 1;
        giftScore[b] -= 1;
    })
    
    
    const len = friends.length;
    
    for (let i = 0; i < len; i++) {
        const a = friends[i];
        for (let j = i + 1; j < len; j++) {
            const b = friends[j];
            
            if (name[a][b] === undefined) name[a][b] = 0;
            if (name[b][a] === undefined) name[b][a] = 0;
            
            
            // 주고받은 기록 x or 같을때
            if (name[a][b] === name[b][a]) {
                if (giftScore[a] === giftScore[b]) continue;
                else if (giftScore[a] > giftScore[b]) {
                    next[a] += 1;
                } else next[b] += 1;
            }
            // 주고받은 기록 o
            else {
                if (name[a][b] > name[b][a]) next[a] += 1;
                else next[b] += 1;
            }
        }
    }
    const answer = Math.max(...Object.values(next));
    return answer;
}