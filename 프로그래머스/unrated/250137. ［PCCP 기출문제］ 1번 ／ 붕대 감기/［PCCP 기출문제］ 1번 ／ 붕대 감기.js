function heal(health, healing, current) {
    if (healing <= 0)
        return current;
    current = current + healing;
    if (current >= health)
        current = health;
    return current;
}

function solution(bandage, health, attacks) {
    // 붕대 정보 [시전시간, 1초당 회복량 x, 추가 회복량 y], 최대 체력, [공격 시간,피해량]
    let answer = 0; // 남은 체력
    // t * x 체력 회복 연속으로 붕대 감기 성공하면 t * x + y
    // 최대 체력이 존재해 현재 체력이 최대 체력보단 작음
    // 공격 당하면 취소 && 회복 x && 체력 다운 + 붕대감기 다시 사용해서 연속 성공시간 0
    // 0 이하면 죽음

    let time = 0;
    const maxHealth = health;
    
    while(attacks.length != 0)
    {
        const prev = time;
        const next = time + bandage[0];
        if (attacks[0][0] > prev && attacks[0][0] <= next) {
            const damage = attacks.shift();
            time = damage[0];
            const healing = (damage[0] - prev - 1) * bandage[1];
            health = heal(maxHealth, healing, health);
            health -= damage[1];
            if (health <= 0)
                return -1;
        } else {
            const healing = (bandage[0] * bandage[1]) + bandage[2];
            health = heal(maxHealth, healing, health);
            time += bandage[0];
        }
    }
    return health;
}