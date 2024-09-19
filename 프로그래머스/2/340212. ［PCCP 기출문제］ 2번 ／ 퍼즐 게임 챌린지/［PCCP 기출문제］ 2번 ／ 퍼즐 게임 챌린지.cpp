#include <string>
#include <vector>
#include <iostream>

using namespace std;

long long solve(long long level, int diff, int prev, int cur) {
    if (level >= diff) return cur;
    
    return (diff - level) * (prev + cur) + cur;
}

int solution(vector<int> diffs, vector<int> times, long long limit) {
    int answer = 0;
    int len = times.size();
    
    long long maxValue = -1;
    long long left = 1;
    long long right = limit;
    

    
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        
        long long result = times[0];
        for (int i = 1; i < len; i++) {
            result += solve(mid, diffs[i], times[i - 1], times[i]);
        }

        
        if (result <= limit) {
            maxValue = mid;
            right = mid -1;
        } else {
            left = mid + 1;
        }
    }
    answer = maxValue;
    return answer;
}