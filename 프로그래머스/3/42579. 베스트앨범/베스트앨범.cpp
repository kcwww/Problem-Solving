#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    unordered_map<string, int> m;
    unordered_map<string, vector<pair<int, int>>> g;
    

    for (int i = 0; i < genres.size(); i++) {
        m[genres[i]] += plays[i];
        g[genres[i]].push_back({plays[i], i});
    }
    

    vector<pair<string, int>> total(m.begin(), m.end());
    

    sort(total.begin(), total.end(), [](pair<string, int> &a, pair<string, int> &b) {
        return b.second < a.second;
    });
    

    for (auto &t : total) {
        string genre = t.first;
        vector<pair<int, int>> &arr = g[genre];
        

        sort(arr.begin(), arr.end(), [](pair<int, int> &a, pair<int, int> &b) {
            if (a.first == b.first) return a.second < b.second;
            return a.first > b.first;
        });
        

        for (int j = 0; j < min(2, (int)arr.size()); j++) {
            answer.push_back(arr[j].second);
        }
    }
    
    return answer;
}