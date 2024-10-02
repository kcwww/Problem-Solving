#include <iostream>
#include <vector>
using namespace std;

int getRange(int w) {
    return 2 * w + 1;
}

int getStation(int range, int w) {
    int div = getRange(w);
    int quotient = range / div;
    int remain = range % div;
    quotient += remain != 0 ? 1 : 0;
    return quotient;
}

int solution(int n, vector<int> stations, int w)
{
    int answer = 0;

    int start = stations[0] - w;
    if (start > 1) {
       answer += getStation(start - 1, w);
    }
    
    for (int i = 1; i < stations.size(); i++) {
        int range = stations[i] - stations[i - 1] - (2 * w) - 1;
        if (range > 0)
            answer += getStation(range, w);
    }
    
    
    int last = stations.back() + w;
    if (last < n) {
        answer += getStation(n - last, w);
    }

    return answer;
}