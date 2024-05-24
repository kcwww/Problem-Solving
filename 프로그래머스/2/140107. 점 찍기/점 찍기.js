const findMax = (i, d, k) => {
    if (i % k !== 0) return 0;
    
    const y = Math.floor(Math.sqrt(d*d - i*i));
    const maxY = Math.floor(y / k) * k;
    
    
    return (maxY / k + 1);
}

const solution = (k, d) => {
    // a * k b * k
    // 원점과 거리가 d 가 넘으면 점을 찍지 않음
    
    // 반지름이 d 인 원 내부의 점의 개수 & k 의 배수 리턴
    
    let answer = 0;
    
    for (let i = 0; i <= d; i++) {
        
        answer += findMax(i, d, k);
    }
    
    
    
    return answer;
}