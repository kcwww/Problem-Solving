function solution(r1, r2) {
    let answer = 0;
    
    // x값에 따른 y값 만들어, 조건 확인
    for (let i = 1; i < r2; i++) {
        if (r1 > i) {
            let min_y = Math.pow(r1, 2) - Math.pow(i, 2);
            let max_y = Math.pow(r2, 2) - Math.pow(i, 2);

            if (min_y >= 0 && max_y >= 0) {
                min_y = Math.sqrt(min_y);
                max_y = Math.sqrt(max_y);

                min_y = Math.ceil(min_y); // 올림
                max_y = Math.floor(max_y); // 버림

                answer += max_y - min_y + 1;
            }
        } else {
            let max_y = Math.floor(Math.sqrt(Math.pow(r2, 2) - Math.pow(i, 2)));
            answer += max_y + 1;
        }
    }
    
    answer += 1;
    answer *= 4;

    return answer;
}
