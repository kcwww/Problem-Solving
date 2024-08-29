#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int n = triangle.size();
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < triangle[i].size(); j++) {
            if (j == 0) triangle[i][0] += triangle[i - 1][0];
            else if (j == i) triangle[i][j] += triangle[i - 1][j - 1];
            else triangle[i][j] += max(triangle[i -1][j - 1], triangle[i - 1][j]);
        }
    }
    
    return *max_element(triangle[n - 1].begin(), triangle[n - 1].end());
}