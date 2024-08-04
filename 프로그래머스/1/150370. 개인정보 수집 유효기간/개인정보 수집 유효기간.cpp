#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<string> split(const string &str, char delimeter) {
    vector<string> result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, delimeter)) result.push_back(token);
    return result;
}

int transformDate(const string & Date) {
    vector<string> parseDate = split(Date, '.');
    return stoi(parseDate[0]) * 12 * 28 + stoi(parseDate[1]) * 28 + stoi(parseDate[2]);
}

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    unordered_map<string, int> termsMap;
    int todayNum = transformDate(today);
    for (const auto &term : terms) {
        vector<string> parsedTerm = split(term, ' ');
        termsMap[parsedTerm[0]] = stoi(parsedTerm[1]) * 28;
    }
    
    for (int i = 0; i < privacies.size(); i++) {
        vector<string> privacy = split(privacies[i], ' ');
        int dateNum = transformDate(privacy[0]) + termsMap[privacy[1]];
        if (todayNum >= dateNum) answer.push_back(i + 1);
    }
    
    return answer;
}