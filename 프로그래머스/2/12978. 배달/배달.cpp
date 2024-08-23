#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

void dijkstra(int N, vector<int> &dist, vector<vector<pair<int, int>>> &village) {

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    

    dist[1] = 0;
    pq.push({0, 1});

    while (!pq.empty()) {
        int current_distance = pq.top().first;
        int current_node = pq.top().second;
        pq.pop();


        if (current_distance > dist[current_node]) continue;


        for (auto &neighbor : village[current_node]) {
            int next_node = neighbor.first;
            int edge_weight = neighbor.second;
            int new_distance = current_distance + edge_weight;


            if (new_distance < dist[next_node]) {
                dist[next_node] = new_distance;
                pq.push({new_distance, next_node});
            }
        }
    }
}

int solution(int N, vector<vector<int>> road, int K) {
    int answer = 0;
    

    vector<vector<pair<int, int>>> village(N + 1);
    vector<int> distance(N + 1, numeric_limits<int>::max());


    for (const auto &r : road) {
        int from = r[0];
        int to = r[1];
        int dist = r[2];
        village[from].emplace_back(to, dist);
        village[to].emplace_back(from, dist);
    }


    dijkstra(N, distance, village);


    for (int i = 1; i <= N; i++) {
        if (distance[i] <= K) {
            answer++;
        }
    }

    return answer;
}
