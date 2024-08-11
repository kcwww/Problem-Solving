#include <string>
#include <vector>
#include <iostream>

using namespace std;

int gcd(int a, int b) {
    int r = b % a;
    if (r == 0) return a;
    return gcd(r, a);
}

int solution(vector<int> arrayA, vector<int> arrayB) {
    int answer = arrayA[0];
    for (const auto &A : arrayA) {
        answer = gcd(answer, A);
    }
    
    bool flag = false;
    int gcd_b = arrayB[0];
    for (const auto &B : arrayB) {
        gcd_b = gcd(gcd_b, B);
        if (B % answer == 0) flag = true;
    }
    
    
    for (const auto &A: arrayA) {
        if (flag && A % gcd_b == 0) return 0;
    }
    
    return answer > gcd_b ? answer : gcd_b;
}