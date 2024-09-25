#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    // 우선순위 큐
    // 앞 요소부터 n 만큼 변경하기
    priority_queue<int> pq(works.begin(), works.end());
    
    while (n > 0) {
        int work = pq.top();
        if (work == 0) break;
        pq.pop();
        pq.push(work - 1);
        n--;
    }
    
    while (!pq.empty()) {
        long work = pq.top();
        pq.pop();
        answer += (work * work);
    }
    return answer;
}