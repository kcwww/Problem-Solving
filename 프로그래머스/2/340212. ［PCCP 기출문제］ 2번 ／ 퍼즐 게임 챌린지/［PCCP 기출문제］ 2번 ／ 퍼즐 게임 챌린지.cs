using System;

public class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        // 1. 이분 탐색의 범위 설정
        int left = 1;         // 숙련도 최솟값
        int right = 100000;   // 제한사항 기준 퍼즐의 최대 난이도 (이 이상 숙련도를 올릴 필요가 없음)
        
        // 2. 이분 탐색 (Parametric Search) 시작
        while (left <= right) {
            int mid = (left + right) / 2; // 이번 턴에 테스트해 볼 숙련도(x)
            
            // 해당 숙련도로 시간 내에 풀 수 있는지 확인
            if (IsPossible(mid, diffs, times, limit)) {
                answer = mid;       // 풀 수 있다면 정답 후보에 기록
                right = mid - 1;    // "더 낮은 숙련도로도 될까?" -> 범위를 낮춰서 재탐색
            } else {
                left = mid + 1;     // 못 푼다면 "숙련도를 더 올려야 해!" -> 범위를 높여서 재탐색
            }
        }
        
        return answer;
    }
    
    // 3. 특정 숙련도(level)로 퍼즐을 끝까지 풀었을 때 limit 안에 들어오는지 확인하는 헬퍼 메서드
    private bool IsPossible(int level, int[] diffs, int[] times, long limit) {
        long totalTime = 0;
        
        for (int i = 0; i < diffs.Length; i++) {
            if (diffs[i] <= level) {
                // 숙련도가 충분할 때: 현재 퍼즐 시간만 소모
                totalTime += times[i];
            } else {
                // 숙련도가 부족해서 틀릴 때
                int mistakes = diffs[i] - level; // 틀리는 횟수
                int timePrev = (i == 0) ? 0 : times[i - 1]; // 0번째 퍼즐은 이전 시간이 없으므로 0 처리
                
                // 공식: 틀린 횟수 * (현재 시간 + 이전 시간) + 다시 제대로 푸는 시간(현재 시간)
                totalTime += (long)mistakes * (times[i] + timePrev) + times[i];
            }
            
            // [최적화] 계산 도중 이미 limit을 넘었다면 더 볼 필요 없이 실패(false) 반환
            if (totalTime > limit) return false;
        }
        
        // 끝까지 풀었는데 limit 안쪽이면 성공!
        return true; 
    }
}