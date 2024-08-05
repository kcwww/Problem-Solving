#include <string>
#include <vector>
#include <queue>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    queue <string> q;
    queue <string> q2;
    
    for (const auto &card : cards1) q.push(card);
    for (const auto &card : cards2) q2.push(card);
    
    string answer = "Yes";
    
    for (const auto &g : goal) {
        if (g == q.front()) q.pop();
        else if (g == q2.front()) q2.pop();
        else return "No";
    }
    return answer;
}