#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


vector<int> solution(int n, int s) {
    vector<int> answer;
    
    if (n > s) return vector<int> (1, -1);

    int quotient = s / n;
    int remain = s % n;
    
    for (int i = 0; i < n; i++) answer.push_back(quotient);
    
    int idx = 0;
    while (remain > 0) {
        answer[idx] += 1;
        remain--;
        idx++;
    }
    sort(answer.begin(), answer.end(), [](int a, int b){ return a < b; });
    return answer;
}