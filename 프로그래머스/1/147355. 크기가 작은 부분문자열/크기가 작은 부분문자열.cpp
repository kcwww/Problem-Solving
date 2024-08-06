#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int size = p.size();
    unsigned long long number = stoull(p);
    
    
    for (int i = 0; i <= t.size() - size; i++) {
        unsigned long long result = stoull(t.substr(i, size));
        if (number >= result) answer += 1;
    }
    return answer;
}