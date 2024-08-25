#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(vector<int> sequence) {
    long long oddAnswer = sequence[0];
    long long oddCurrent = sequence[0];
    long long evenAnswer = -sequence[0];
    long long evenCurrent = -sequence[0];
    
    for (int i = 1; i < sequence.size(); i++) {
        long long oddElement = sequence[i] * (i % 2 == 0 ? 1 : -1);
        long long evenElement = sequence[i] * (i % 2 == 0 ? -1 : 1);
        
        oddCurrent = max(oddElement, oddElement + oddCurrent);
        oddAnswer = max(oddAnswer, oddCurrent);
        evenCurrent = max(evenElement, evenElement + evenCurrent);
        evenAnswer = max(evenAnswer, evenCurrent);
    }
    
    return max(evenAnswer, oddAnswer);
}
