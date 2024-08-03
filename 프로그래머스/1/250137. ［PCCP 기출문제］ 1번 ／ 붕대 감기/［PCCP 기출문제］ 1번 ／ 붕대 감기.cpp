#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    // t초 동안 붕대를 감으며 1 초마다 x 만큼 체력 회복
    // 연속으로 성공하면 + y
    // 몬스터에게 당하면 기술이 취소됨, 당하는 순간은 회복 x
    // 체력 0 이하면 정지 -1
    // 남은 체력 리턴
    
    // 시작시간 0 으로 초기화
    // 어택을 순회하며 시작시간이랑 비교
    // 비교시 체력 재조정
    
    int time = 0;
    int atk = 0;
    int cnt = 0;
    const int maxHealth = health;
    const int binding = bandage[0];
    const int healing = bandage[1];
    const int success = bandage[2];
    while (atk < attacks.size()) {
        time += 1;
        cnt += 1;
        if (attacks[atk][0] == time) {
            health -= attacks[atk][1];
            atk += 1;
            cnt = 0;
        }
        else { 
            health += healing;
            if (cnt == binding) {
                health += success;
                cnt = 0;
            }
        }
        
        if (health >= maxHealth) health = maxHealth;
        else if (health <= 0) {
            health = -1;
            break ;
        }
    }
    return health;
}