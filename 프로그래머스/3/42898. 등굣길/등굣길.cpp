#include <string>
#include <vector>
#include <queue>



using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    vector<vector<long long>> map;
    for (int i = 0; i < n; i++) {
        map.push_back(vector<long long>(m, 0));
    }
    
    for (auto puddle: puddles) {
        int row = puddle[1] - 1;
        int col = puddle[0] - 1;
        
        map[row][col] = -1;
    }
    
    bool flag = false;
    for (int i = 0; i < m; i++) {
        if (flag) {
            map[0][i] = 0;
            continue;
        }
        
        if (map[0][i] == -1) {
            map[0][i] = 0;
            flag = true;
            continue;
        }
        
        map[0][i] = 1;
    }
    
    flag = false;
    for (int i = 0; i < n; i++) {
        if (flag) {
            map[i][0] = 0;
            continue;
        }
        
        if (map[i][0] == -1) {
            map[i][0] = 0;
            flag = true;
            continue;
        }
        map[i][0] = 1;
    }
    
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (map[i][j] == -1) map[i][j] = 0;
            else {
                map[i][j] = map[i - 1][j] + map[i][j - 1] % 1000000007;
            }
        }
    }
    return map[n - 1][m - 1] % 1000000007;
}