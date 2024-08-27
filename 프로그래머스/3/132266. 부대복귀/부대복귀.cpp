#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {

    vector<vector<int>> graph(n + 1);
    vector<int> costs(n + 1, -1);
    queue<int> q;


    for (const auto& road : roads) {
        int n1 = road[0];
        int n2 = road[1];
        graph[n1].push_back(n2);
        graph[n2].push_back(n1);
    }


    costs[destination] = 0;
    q.push(destination);


    while (!q.empty()) {
        int current = q.front();
        q.pop();
        for (int neighbor : graph[current]) {
            if (costs[neighbor] == -1) {
                q.push(neighbor);
                costs[neighbor] = costs[current] + 1;
            }
        }
    }

    vector<int> answer;
    for (int source : sources) {
        answer.push_back(costs[source]);
    }

    return answer;
}