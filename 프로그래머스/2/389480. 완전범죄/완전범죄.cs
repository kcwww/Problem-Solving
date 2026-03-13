using System;

public class Solution {
    public int solution(int[,] info, int n, int m) {
        int length = info.GetLength(0);
        int[,] dp = new int[length + 1, n];
        int NONE = -1;
        
        for (int i = 0; i <= length; i++) {
            for (int j = 0; j < n; j++) {
                dp[i, j] = NONE;
            }
        }
        
        dp[0, 0] = 0;
        
        
        for (int i = 0; i < length; i++) {
            int traceA = info[i, 0];
            int traceB = info[i, 1];
            
            // 현재 물건(i)을 훔치기 위해, 이전 단계의 모든 A흔적(j) 세이브 파일을 열어봅니다.
            for (int j = 0; j < n; j++) {
                
                // 세이브 파일이 비어있다면(-1) 도달할 수 없는 우주이므로 스킵!
                if (dp[i, j] == NONE) continue;
                
                // --- [A가 훔칠 때] ---
                int nextTraceA = j + traceA;
                // A의 흔적이 n 이상이 되면 안 되므로 조건문으로 방어합니다.
                if (nextTraceA < n) {
                    // 다음 칸이 비어있거나(-1), 기존 값보다 지금 가져가는 B의 흔적(dp[i, j])이 더 작다면 갱신!
                    if (dp[i + 1, nextTraceA] == NONE || dp[i, j] < dp[i + 1, nextTraceA]) {
                        dp[i + 1, nextTraceA] = dp[i, j];
                    }
                }
                
                // --- [B가 훔칠 때] ---
                // A의 흔적은 그대로 j, B의 흔적은 기존 B흔적에 traceB를 더합니다.
                int nextTraceB = dp[i, j] + traceB;
                
                // 다음 칸이 비어있거나(-1), 기존 값보다 새로 계산한 B의 흔적(nextTraceB)이 더 작다면 갱신!
                if (dp[i + 1, j] == NONE || nextTraceB < dp[i + 1, j]) {
                    dp[i + 1, j] = nextTraceB;
                }
            }
        }
        
        // 모든 물건(length)을 훔친 상태에서 확인
        for (int j = 0; j < n; j++) {
            // 세이브 파일이 존재하고 && B의 흔적이 경찰 출동 조건(m)보다 작다면 성공
            if (dp[length, j] != NONE && dp[length, j] < m) {
                // j는 0부터 순서대로 올라가므로, 가장 먼저 조건을 만족하는 j가 무조건 최솟값입니다.
                return j; 
            }
        }
        
        // 어떻게 훔쳐도 둘 다 안 잡히는 경우가 없다면 -1 반환
        return -1;
    }
}