#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    vector<vector<int>> triangle;
    
    for (int i = 0; i < n; i++) {
        triangle.push_back(vector<int> (i + 1, 0));
    }
    
    int row = -1, col = 0, num = 1;
    
    while (n > 0) {
        
        for (int i = 0; i < n; i++) {
            row++;
            triangle[row][col] = num;
            num++;
        }
        
        for (int i = 0; i < n - 1; i++) {
            col++;
            triangle[row][col] = num;
            num++;
        }
        
        for (int i = 0; i < n - 2; i++) {
            row--;
            col--;
            triangle[row][col] = num;
            num++;
        }
        
        n -= 3;
    }
    
    for (int i = 0; i < triangle.size(); i++) {
        for (int j = 0; j < triangle[i].size(); j++) {
            answer.push_back(triangle[i][j]);
        }
    }
    
    return answer;
}