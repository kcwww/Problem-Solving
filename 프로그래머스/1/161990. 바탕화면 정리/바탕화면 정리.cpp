#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    vector<int> answer = {51,51,0,0};
    int row = wallpaper.size();
    int col = wallpaper[0].size();
    
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (wallpaper[i][j] == '#') {
                answer[0] = answer[0] < i ? answer[0] : i;
                answer[1] = answer[1] < j ? answer[1] : j;
                answer[2] = answer[2] > i + 1 ? answer[2] : i + 1;
                answer[3] = answer[3] > j + 1 ? answer[3] : j + 1;
            }
        }
    }
    return answer;
}