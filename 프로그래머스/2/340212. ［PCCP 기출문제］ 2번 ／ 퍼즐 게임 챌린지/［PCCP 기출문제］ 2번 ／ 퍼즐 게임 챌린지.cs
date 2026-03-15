using System;

public class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        
        int left = 1;
        int right = 100000;
        
        
        while (left <= right) {
            int mid = (left + right) / 2;
            
            
            if (IsPossible(mid, diffs, times, limit)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return answer;
    }
    
    
    private bool IsPossible(int level, int[] diffs, int[] times, long limit) {
        long totalTime = 0;
        
        for (int i = 0; i < diffs.Length; i++) {
            if (diffs[i] <= level) {
                totalTime += times[i];
            } else {
                int mistakes = diffs[i] - level; 
                int timePrev = times[i - 1];
                
                // 틀린 횟수 * (현재 시간 + 이전 시간) + 다시 제대로 푸는 시간(현재 시간)
                totalTime += (long)mistakes * (times[i] + timePrev) + times[i];
            }
            
            if (totalTime > limit) return false;
        }
        
        return true; 
    }
}