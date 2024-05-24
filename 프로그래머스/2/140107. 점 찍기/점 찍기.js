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
    
    // 기울기 1 이하인 가장 큰 점 찾고 그 점만큼 * 2
    // 기울기 1 인 점 찾기
    let answer = 0;
    
    for (let i = 0; i <= d; i++) {
        const distance = Math.sqrt(2*i*i)
        
        
        
        // 직선 아래 가장 큰점 * 2
        answer += findMax(i, d, k);
    }
    
    
    
    return answer;
}