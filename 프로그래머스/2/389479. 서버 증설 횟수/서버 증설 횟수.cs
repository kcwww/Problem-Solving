using System;

public class Solution {
    public int solution(int[] players, int m, int k) {
        // m 명당 서버 1대
        // n x m 명이상 (n + 1) x m 명 미만이라면 최소 n 대의 증설된 서버가 운영
        // 한번 증설한 서버는 k 시간동안 운영하고 반납
        
        // 현재 증설된 서버 수 x m 만큼 수용가능 증설된 서버는 인덱스 수 (시간) 만큼 운영하고 꺼짐.
        // 순회하면서 증설된 서버 시간 종료 확인 -> 이용자 수 확인 -> 서버 증설 유무 확인 후 증설 횟수 카운트
        // 시간대 배열 24 -> 서버가 켜질때 해당 배열 요소들을 +1 씩 해주자.
        int answer = 0;
        int[] server = new int [24];
        
        for (int i = 0; i < 24; i++) {
            
            // 필요한 서버 갯수
            int requiredServer = players[i] / m;
            
            // 현재 켜져있는 서버보다 필요한 서버가 많다면
            if (requiredServer > server[i]) {
                // 서버 증설
                int newServer = requiredServer - server[i];
                answer += newServer;
                
                for (int j = i; j < i + k; j++) {
                    
                    if (j >= 24) break;
                    server[j] += newServer;
                }
            }
        }
        
        
        return answer;
    }
}