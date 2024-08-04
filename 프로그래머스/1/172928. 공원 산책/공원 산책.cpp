#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

vector<string> split(const string &str, char delimeter) {
    vector<string> result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delimeter)) result.push_back(token);
    return result;
}

vector<int> getPosition(vector<string> park) {
    vector<int> position = {0, 0};
    for (int i = 0; i < park.size(); i++) {
        for (int j = 0; j < park[0].size(); j++) {
            if (park[i][j] == 'S') {
                position[0] = i;
                position[1] = j;
                return position;
            };
        }
    }
    return position;
}

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer = getPosition(park);
    int row = park.size();
    int col = park[0].size();
    
    
    
    for (int i = 0; i < routes.size(); i++) {
        vector<string> sp = split(routes[i], ' ');
        int num = stoi(sp[1]);
        int r = answer[0];
        int c = answer[1];
        bool flag = true;
        while (num > 0) {
            if (sp[0] == "E") c++;
            else if (sp[0] == "S") r++;
            else if (sp[0] == "W") c--;
            else if (sp[0] == "N") r--;
            
            if (!(r >= 0 && r < row && c >= 0 && c < col && park[r][c] != 'X')) {
                flag = false;
                break;
            }
            num--;
        }
        if (flag) {
            answer[0] = r;
            answer[1] = c;
        }
        
    }
    
    return answer;
}