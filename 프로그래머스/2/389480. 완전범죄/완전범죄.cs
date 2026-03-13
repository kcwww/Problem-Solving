using System;

public class Solution {
    public int solution(int[,] info, int n, int m) {

        int NONE = -1;
        int length = info.GetLength(0);
        int[,] dp = new int[length + 1, n];
        
        // dp 초기화
        for (int i = 0; i <= length; i++) {
            for (int j = 0; j < n; j++) {
                dp[i, j] = NONE;
            }
        }
        
        dp[0, 0] = 0;
        
        for (int i = 0; i < length; i++) {
            int traceA = info[i, 0];
            int traceB = info[i, 1];
            
            for (int j = 0; j < n; j++) {
                if (dp[i, j] == NONE) continue;
                
                // a 가 훔칠때
                int nextTraceA = traceA + j;
                
                
                if (nextTraceA < n) {
                    int futureB = dp[i, j];
                    int recordedB = dp[i + 1, nextTraceA];
                    if (dp[i + 1, nextTraceA] == NONE || futureB < recordedB) {
                        dp [i + 1, nextTraceA] = futureB;
                    }
                }
                
                // b가 훔칠때
                int nextTraceB = dp[i, j] + traceB;
                if (nextTraceB < m) {
                    if (dp[i + 1, j] == NONE || nextTraceB < dp[i + 1, j]) {
                        dp[i + 1, j] = nextTraceB;
                    }
                }
                
            }
            
            
            
        }
        
        for (int j = 0; j < n; j++) {
            if (dp[length, j] != NONE && dp[length, j] < m) {
                return j;
            }
        }
        
        return -1;
    }
}