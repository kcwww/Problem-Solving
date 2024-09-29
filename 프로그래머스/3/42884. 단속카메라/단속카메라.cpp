#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 1;
    // 끝나는 시간으로 정렬
    // 끝나는 시간 기준 카메라 설치 -> 설치된 위치 기준 다음 탐색
    
        
    sort(routes.begin(), routes.end(), [](vector<int> a, vector<int> b) {
        return a[1] < b[1];
    });
    
    int lastest = routes[0][1];
    for (auto route : routes) {
        if (lastest >= route[0] && lastest <= route[1]) continue;
        lastest = route[1];
        answer += 1;
    }
    
    
    return answer;
}