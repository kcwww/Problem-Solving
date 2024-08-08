#include <string>
#include <vector>

using namespace std;

int getWeapon(int num, int limit, int power) {
    int result = 0;
    for (int i = 1; i * i <= num; i++) {
        if ((i * i) == num) result += 1;
        else if (num % i == 0) result += 2;
    }
    if (result > limit) return power;
    return result;
}

int solution(int number, int limit, int power) {
    int answer = 0;
    for (int i = 1; i <= number; i++) {
        int cnt = getWeapon(i, limit, power);
        answer += cnt;
    }
    return answer;
}