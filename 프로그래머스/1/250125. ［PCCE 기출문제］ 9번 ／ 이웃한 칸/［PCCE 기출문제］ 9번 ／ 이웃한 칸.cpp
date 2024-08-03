#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<string>> board, int h, int w) {
    int answer = 0;
    int width = board[0].size();
    int height = board.size();
    const string &color = board[h][w];
    const std::vector<std::vector<int>> direction = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (const auto &dir : direction) {
        const int x = w + dir[1];
        const int y = h + dir[0];
        
        if (x >= 0 && x < width && y >= 0 && y < height) {
            if (board[y][x] == color) answer += 1;
        }
    }
    return answer;
}