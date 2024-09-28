#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    
    sort(A.begin(), A.end(), [](int a, int b) {
        return a > b;
    });
    
    sort(B.begin(), B.end(), [](int a, int b) {
        return a > b;
    });
    
    int N = A.size();
    
    for (int i = 0, j = 0; i < N; i++, j++) {
        
        if (A[i] < B[j]) answer += 1;
        else j--;
    }
    return answer;
}