using System;

public class Solution {
    int answer = 0;
    
    int[,] queries;
    int[] answers;
    int length = 0;
    
    public void MakeCombination(int start, int end, int depth, int[] arr) {
        if (depth == 5) {
            CheckCode(arr);
            return;
        }
        
        for (int i = start; i <= end; i++) {
            arr[depth] = i;
            MakeCombination(i + 1, end, depth + 1, arr);
        }
    }
    
    
    public void CheckCode(int[] arr) {
        bool flag = true;
        for (int i = 0; i < length; i++) {
            int validation = 0;
            
            for (int k = 0; k < 5; k++) {
                for (int m = 0; m < 5; m++) {
                    if (arr[k] == queries[i, m]) {
                        validation++;
                    }
                }
            }
            
            if (validation != answers[i]) {
                flag = false;
                break;
            }
            
        }
        if (flag) answer++;
    }
    
    public int solution(int n, int[,] q, int[] ans) {
        // 완전탐색
        queries = q;
        answers = ans;
        length = ans.Length;
        
        int[] a = new int[5];
        MakeCombination(1, n, 0, a);
        
        return answer;
    }
}