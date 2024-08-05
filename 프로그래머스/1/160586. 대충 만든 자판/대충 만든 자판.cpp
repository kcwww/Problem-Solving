#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    unordered_map <char, int> key;
    
    for (const auto &keys : keymap) {
        for (int i = 0; i < keys.size(); i++) {
            if (key.find(keys[i]) != key.end()) key[keys[i]] = min(key[keys[i]], i + 1);
            else key[keys[i]] = i + 1;
        }
    }
    

    
    for (const auto &target : targets) {
        int cnt = 0;
        for (const auto &charset : target) {
            if (key.find(charset) == key.end()) {
                cnt = -1;
                break;
            }
            cnt += key[charset];
        }
        answer.push_back(cnt);
    }
    return answer;
}