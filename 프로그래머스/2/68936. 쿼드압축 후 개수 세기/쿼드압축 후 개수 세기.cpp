#include <string>
#include <vector>
#include <iostream>

using namespace std;

int checkArea(vector<vector<int>> &quad) {
    int length = quad.size();
    int init = quad[0][0];
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            if (quad[i][j] != init) return -1;
        }
    }
    return init;
}

vector<vector<int>> makeHalfVector(int start, int row, int half, vector<vector<int>> &arr) {
    vector<vector<int>> result;

    for (int i = 0; i < half; i++) {
        vector<int> temp(arr[row + i].begin() + start, arr[row + i].begin() + start + half);
        result.push_back(temp);
    }
    return result;
}

void printVector(vector<vector<int>> &vec) {
    for (int i = 0; i < vec.size(); i++) {
        for (int j = 0; j < vec[0].size(); j++) {
            cout << vec[i][j] << " ";
        }
        cout << endl;
    }
}

void quadTree(vector<vector<int>> &arr, vector<int> &answer) {
    int num = checkArea(arr);
    if (num != -1) {
        answer[num]++;
        return;
    }

    int length = arr.size();
    if (length == 1) {
        answer[arr[0][0]]++;
        return;
    }
    int half = length / 2;
    
    for (int i = 0; i <= half; i += half) { 
        for (int j = 0; j <= half; j += half) {
            vector<vector<int>> temp = makeHalfVector(i, j, half, arr);
            quadTree(temp, answer);
        }
    }
}

vector<int> solution(vector<vector<int>> arr) {

    vector<int> answer(2, 0);
    quadTree(arr, answer);
    return answer;
}