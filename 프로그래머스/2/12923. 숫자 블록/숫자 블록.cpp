#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(long long begin, long long end) {
    vector<int> answer;
    
    for (long long i = begin; i <= end; i++) {
        if (i == 1) { answer.push_back(0); continue; }
        
        long long div = 1;
        for (long long j = 2; j * j <= i; j++) {
            if (i % j == 0) { 
                div = j;
                if (i / j <= 10000000) { div = i / j; break; }
            }
        }
        answer.push_back(div);
    }
    return answer;
}