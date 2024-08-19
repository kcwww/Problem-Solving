#include <vector>
#include <iostream>
#include <queue>

using namespace std;

void bfs(int i, int j, vector<vector<int>> &picture, vector<int> &answer, int row, int col) {
    const int area = picture[i][j];
    const vector<vector<int>> dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    answer[0] += 1;
    
    vector<int> first = {i,j};
    queue<vector<int>> q;
    q.push(first);
    
    int maxNum = 0;
    while(q.size() > 0) {
        vector<int> e = q.front();
        q.pop();
        maxNum += 1;
        picture[e[0]][e[1]] = 0;
        
        for (int k = 0; k < 4; k++) {
            int r = e[0] + dir[k][0];
            int c = e[1] + dir[k][1];
            
            if (r >= 0 && r < row && c >= 0 && c < col && picture[r][c] == area) {
                picture[r][c] = 0;
                vector<int> next = {r, c};
                q.push(next);
            }
        }
    }
    answer[1] = max(answer[1], maxNum);
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    // bfs 로 넓이 구하기
    // 탐색할때 첫 장소 기억
    vector<int> answer = {0, 0};
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] != 0) bfs(i, j, picture, answer, m, n);
            
        }
    }
    return answer;
}