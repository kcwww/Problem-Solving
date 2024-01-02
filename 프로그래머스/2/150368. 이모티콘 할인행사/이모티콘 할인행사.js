function discount(emoticons) {
    const dc = [10, 20, 30, 40];
    
    const result = emoticons.map((element) => {
        const discountedArray = dc.map((ele) => {
            return (100 - ele) * (element / 100);
        })
        return discountedArray;
    });
    return result;
}

function checkUser(cur, users) {
    let plus = 0;
    let uSum = 0;
    
    users.forEach((e) => {
        const userBuy = e[0];
        const userPlus = e[1];
        let sum = 0;
        
        cur.forEach((ele) => {
            const price = ele[0];
            const dis = ele[1];
            
            if (dis >= userBuy) {
                sum += price;
            }
        });
       if (sum >= userPlus) {
           plus += 1;
       } else {
           uSum += sum;
       }
    });
    return [plus, uSum];
}

function dfs(number, emoticons, users, idx, result, cur) {

    if (idx === (number)) {
        const [plus, price] = checkUser(cur, users);

        
        if (plus > result[0]) {
            result[0] = plus;
            result[1] = price;
        } else if (plus === result[0]) {
            result[1] = (result[1] >= price ? result[1] : price);
        }
        
        return ;
    }
    
    for (let i = 0; i < 4; i++) {
        cur[idx] = [emoticons[idx][i], (i + 1) * 10];
        dfs(number, emoticons, users, idx + 1, result, cur);
    }
};

function solution(users, emoticons) {
    // 이모티콘 m 개 판매
    // 이모티콘 마다 할인율 4개 적용한 배열 만들기
    // dfs 로 모든 조건 탐색
    const eNumber = emoticons.length;
    const dcEmoticons = discount(emoticons);
    const result = [0, 0];
    const cur = new Array(eNumber).fill([]);
    
    dfs(eNumber, dcEmoticons, users, 0, result, cur);
    return result;
}