#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> scores) {
    int answer = 0;
    int target_a = scores[0][0];
    int target_b = scores[0][1];
    int target_score = target_a + target_b;

    sort(scores.begin(), scores.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[0] == b[0])
            return a[1] < b[1];
        return a[0] > b[0];
    });

    int maxb = 0;

    for (const auto& score : scores) {
        int a = score[0];
        int b = score[1];

        if (target_a < a && target_b < b) {
            return -1;
        }

        if (b >= maxb) {
            maxb = b;
            if (a + b > target_score) {
                answer++;
            }
        }
    }

    return answer + 1;
}
