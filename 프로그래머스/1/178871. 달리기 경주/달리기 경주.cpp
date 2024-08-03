#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <iostream>
using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    unordered_map<string, int> ranking;
    map<int, string> ranking_detail;
    for (int i = 0; i < players.size(); i++) {
        ranking[players[i]] = i + 1;
        ranking_detail[i + 1] = players[i];
    }
    
    for (const auto &call : callings) {
        const int rank = ranking[call];
        ranking[call] -= 1;
        swap(ranking_detail[rank], ranking_detail[rank - 1]);
        const string other = ranking_detail[rank];
        ranking[other] += 1;
        
    }
    
    vector<string> answer;
    for (const auto &rank : ranking_detail) {
        answer.push_back(rank.second);
    }
    return answer;
}