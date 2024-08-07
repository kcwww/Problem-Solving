#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#define MAX 2001

using namespace std;

long long dp[2001];
bool vis[2001];

long long solution(vector<int> weights) {
    long long answer = 0;
    for(auto i : weights)
        dp[i] += 1;
    for(auto i : weights){
        if(dp[i] > 1 && !vis[i]){
            answer +=  dp[i] * (dp[i] - 1) / 2;
            vis[i] = true;
        }
        if(2 * i < MAX && dp[2 * i])
            answer += dp[2 * i];
        if(i % 3 == 0 && i/3 * 4 < MAX && dp[i/3 * 4])
            answer += dp[i/3 * 4];
        if(i % 2 == 0 && i/2 * 3 < MAX && dp[i/2 * 3])
            answer += dp[i/2 * 3];
    } 
    return answer;
}