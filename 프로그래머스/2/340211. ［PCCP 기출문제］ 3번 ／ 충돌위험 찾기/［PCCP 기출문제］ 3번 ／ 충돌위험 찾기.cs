using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[,] points, int[,] routes) {
        int answer = 0;
        
        List<List<int[]>> robots = new List<List<int[]>>();
        int maxTime = 0; // 가장 늦게 끝나는 로봇의 총 이동 시간
        
        // 1. 모든 로봇의 궤적(타임라인) 생성
        for (int i = 0; i < routes.GetLength(0); i++) {
            List<int[]> path = new List<int[]>();
            
            // 맨 처음 출발지 세팅 (0초 위치)
            int startNode = routes[i, 0] - 1;
            int currentR = points[startNode, 0];
            int currentC = points[startNode, 1];
            
            path.Add(new int[] { currentR, currentC });
            
            // 각 로봇이 거쳐야 할 경유지 구간들을 순회
            for (int j = 0; j < routes.GetLength(1) - 1; j++) {
                
                // 이번 구간의 목적지
                int toNum = routes[i, j + 1] - 1;
                int targetR = points[toNum, 0];
                int targetC = points[toNum, 1];
                
                // 목적지를 향해 r 먼저 이동, 그 다음 c 이동
                while (currentR != targetR) {
                    currentR += (currentR < targetR) ? 1 : -1;
                    path.Add(new int[] { currentR, currentC });
                }
                
                while (currentC != targetC) {
                    currentC += (currentC < targetC) ? 1 : -1;
                    path.Add(new int[] { currentR, currentC });
                }
            }
            
            robots.Add(path);
            
            // 모든 로봇 중 가장 긴 타임라인 기록
            if (path.Count > maxTime) {
                maxTime = path.Count;
            }
        }
        
        // 2. 시간대별로 충돌 위험 상황(2대 이상 겹침) 카운트
        for (int t = 0; t < maxTime; t++) {
            
            // 이번 1초 동안 로봇들이 위치한 좌표를 셀 딕셔너리
            // 튜플이나 배열 대신 확실한 String 형태 "r,c" 를 키(Key)로 사용합니다.
            Dictionary<string, int> posCount = new Dictionary<string, int>();
            
            foreach (var path in robots) {
                // 이 로봇이 물류센터를 아직 안 빠져나갔다면
                if (t < path.Count) {
                    int r = path[t][0];
                    int c = path[t][1];
                    string key = r + "," + c; // 예: "3,5"
                    
                    if (!posCount.ContainsKey(key)) {
                        posCount[key] = 0;
                    }
                    posCount[key]++;
                }
            }
            
            // 딕셔너리를 순회하며 2대 이상 모인 곳을 찾아 정답 증가
            foreach (var count in posCount.Values) {
                if (count >= 2) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}