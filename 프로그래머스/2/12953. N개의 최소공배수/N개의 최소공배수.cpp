#include <string>
#include <vector>
#include <iostream>

using namespace std;

int gcd(int a, int b) {
    int x = max(a, b);
    int y = min(a, b);
    int result;
    
    while (y != 0) {
        result = x % y;
        x = y;
        y = result;
    }
    return x;
}

int solution(vector<int> arr) {
    
    if (arr.size() == 1) return arr[0];
    int gcf = (arr[0] * arr[1]) / gcd(arr[0], arr[1]);
    for (int i = 1; i < arr.size(); i++) {
        gcf = (gcf * arr[i]) / gcd(gcf, arr[i]);
    }
    return gcf;
}