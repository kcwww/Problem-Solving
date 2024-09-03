#include <string>
#include <vector>


#include <iostream>

using namespace std;

int checkDiff (string A, string B) {
    int diff = 0;
    
    for (int i = 0; i < A.size(); i++) {
        diff += A[i] != B[i] ? 1 : 0;
    }
    return diff;
}

void dfs(string A, string target, int cnt, vector<int> &visit, vector<string> &words, int &answer) {
    if (A == target) {
        answer = answer == 0 ? cnt : (answer > cnt ? cnt : answer);
        return;
    }
    
    for (int i = 0; i < words.size(); i++) {
        if (checkDiff(A, words[i]) == 1 && visit[i] == 0) {
            visit[i] = 1;
            dfs(words[i], target, cnt + 1, visit, words, answer);
            visit[i] = 0;
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    vector<int> visit(words.size(), 0);
    dfs(begin, target, 0, visit, words, answer);
    
    return answer;
}