#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <sstream>

using namespace std;

vector<string> split(const string &str, char delimeter) {
    string token;
    stringstream ss(str);
    vector<string> result;
    while(getline(ss, token, delimeter)) result.push_back(token);
    return result;
}

int solution(vector<string> friends, vector<string> gifts) {
    // 두 사람이 선물을 주고 받은 기록 -> 더 많은 선물을 준 사람이 받음
    
    // 두 사람이 선물을 주고 받은 기록 X or 같 -> 선물 지수가 더 큰 사람이 작은 사람에게 하나 받
    // 선물 지수 = 준 선물의 수 - 받은 선물의 수
    // 선물 지수도 같으면 주고받지않음
    
    // gift a -> b
    int answer = 0;
    unordered_map<string, int> score;
    unordered_map<string, unordered_map<string, int>> lists;
    
    for (const auto &gift : gifts) {
        vector<string> names = split(gift, ' ');
        const string A = names[0];
        const string B = names[1];
        if (score.find(A) == score.end()) score[A] = 0;
        if (score.find(B) == score.end()) score[B] = 0;
        score[A] += 1;
        score[B] -= 1;
        
        if (lists.find(A) == lists.end()) lists[A] = unordered_map<string, int>();
        if (lists.find(B) == lists.end()) lists[B] = unordered_map<string, int>();
        if (lists[A].find(B) == lists[A].end()) lists[A][B] = 0;
        if (lists[B].find(A) == lists[B].end()) lists[B][A] = 0;
        
        lists[A][B] += 1;
        lists[B][A] -= 1;
    }
    for (const auto &entry : lists) {
        int cnt = 0;
        const string &person = entry.first;
        for (const auto & name : friends) {
            if (person == name) continue;
            
            if (lists[person].find(name) == lists[person].end() || lists[person][name] == 0) { if (score[person] > score[name]) cnt++; }
            else if (lists[person][name] > 0) cnt++;
        }
        answer = answer > cnt ? answer : cnt;
    }
    
    return answer;
}