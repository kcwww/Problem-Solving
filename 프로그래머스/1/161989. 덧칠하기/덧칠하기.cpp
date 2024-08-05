#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    int current = 1;
    
    for (const auto &number : section) {
        if (current > number) continue;
        else if (current < number) current = number;
        current += m;
        answer += 1;
    }
    return answer;
}