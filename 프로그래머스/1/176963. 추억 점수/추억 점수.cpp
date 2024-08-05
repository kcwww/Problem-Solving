#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photos) {
    vector<int> answer;
    unordered_map<string, int> yearningMap;
    for (int i = 0; i < name.size(); i++) {
        yearningMap[name[i]] = yearning[i];
    }

    for (const auto &photo : photos) {
        int cnt = 0;
        for (const auto &name: photo) {
            if (yearningMap.find(name) != yearningMap.end()) cnt += yearningMap[name];
        }
        answer.push_back(cnt);
    }
    return answer;
}


