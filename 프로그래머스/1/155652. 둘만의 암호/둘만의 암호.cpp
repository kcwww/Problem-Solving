#include <string>
#include <unordered_map>
#include <iostream>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    unordered_map<int, bool> skipAlpha;
    
    for (const auto &c : skip) {
        int num = c;
        skipAlpha[c] = true;
    }
    
    for (int i = 0; i < s.size(); i++) {
        int cnt = index;
        int alpha = s[i];
        while (cnt > 0) {
            alpha++;
            if (alpha > 'z') alpha = 'a';
            if (skipAlpha[alpha] == 1) continue;
            cnt--;
        }
        answer += alpha;
    }
    
    return answer;
}
