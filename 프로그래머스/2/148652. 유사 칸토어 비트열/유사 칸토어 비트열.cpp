#include <string>
#include <vector>

using namespace std;


bool is_one(long long l) {
    while (l >= 5) {
        if ((l - 2) % 5 == 0) {
            return false;
        }
        l /= 5;
    }
    return l != 2;
}

int solution(int n, long long l, long long r) {
    int answer = 0;
    for (long long i = l - 1; i < r; ++i) {
        if (is_one(i)) {
            answer++;
        }
    }
    return answer;
}