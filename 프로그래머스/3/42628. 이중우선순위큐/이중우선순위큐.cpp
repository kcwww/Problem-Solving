#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> operations) {
    // 오름차순으로 정렬되는 우선순위 큐 생성 (min heap)
    priority_queue<int, vector<int>, greater<int>> minPq;
    // 내림차순으로 정렬되는 우선순위 큐 생성 (max heap)
    priority_queue<int> maxPq;
    // 각 값이 삭제되었는지 추적할 map
    unordered_map<int, int> valueCount;

    for (string operation : operations) {
        // 공백을 기준으로 명령과 값을 분리
        istringstream iss(operation);
        string cmd;
        int num;
        iss >> cmd >> num;

        // 'I' 명령인 경우 값 추가
        if (cmd == "I") {
            minPq.push(num);
            maxPq.push(num);
            valueCount[num]++;
        }
        // 'D -1' 명령인 경우 최소값 삭제
        else if (cmd == "D" && num == -1) {
            while (!minPq.empty() && valueCount[minPq.top()] == 0) {
                minPq.pop();
            }
            if (!minPq.empty()) {
                valueCount[minPq.top()]--;
                minPq.pop();
            }
        }
        // 'D 1' 명령인 경우 최대값 삭제
        else if (cmd == "D" && num == 1) {
            while (!maxPq.empty() && valueCount[maxPq.top()] == 0) {
                maxPq.pop();
            }
            if (!maxPq.empty()) {
                valueCount[maxPq.top()]--;
                maxPq.pop();
            }
        }
    }

    // 남은 값 중 유효한 최댓값과 최솟값 찾기
    while (!maxPq.empty() && valueCount[maxPq.top()] == 0) {
        maxPq.pop();
    }
    while (!minPq.empty() && valueCount[minPq.top()] == 0) {
        minPq.pop();
    }

    // 우선순위 큐가 비어있다면 [0, 0] 반환
    if (minPq.empty() && maxPq.empty()) {
        return {0, 0};
    }

    return {maxPq.top(), minPq.top()};
}
