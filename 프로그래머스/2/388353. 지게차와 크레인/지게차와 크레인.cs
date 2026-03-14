using System;
using System.Collections.Generic;

public class Solution {
    int length;
    int horizontal;
    char NONE = '#';
    
    // 방향 배열 (상, 하, 좌, 우)
    int[] dr = { -1, 1, 0, 0 };
    int[] dc = { 0, 0, -1, 1 };
    
    public int solution(string[] storage, string[] requests) {
        int answer = 0;
        int n = storage.Length;
        int m = storage[0].Length;
        
        // 1. 패딩된 창고 배열 만들기 (크기를 가로세로 +2씩)
        length = n + 2;
        horizontal = m + 2;
        char[,] map = new char[length, horizontal];
        
        // 초기화: 모두 빈칸으로 채움
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < horizontal; j++) {
                map[i, j] = NONE;
            }
        }
        
        // 정중앙에 컨테이너 배치하고 개수 세기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                map[i + 1, j + 1] = storage[i][j];
                answer++;
            }
        }
        
        // 2. 요청 처리
        foreach (string req in requests) {
            char target = req[0];
            
            if (req.Length == 1) { // 지게차 (외부 접근 가능만)
                
                bool[,] visited = new bool[length, horizontal];
                Queue<(int r, int c)> q = new Queue<(int, int)>();
                List<(int r, int c)> toRemove = new List<(int, int)>(); // 일괄 삭제를 위한 리스트
                
                // [0, 0] (무조건 외부)에서 BFS 시작
                q.Enqueue((0, 0));
                visited[0, 0] = true;
                
                while (q.Count > 0) {
                    var curr = q.Dequeue();
                    
                    for (int i = 0; i < 4; i++) {
                        int nr = curr.r + dr[i];
                        int nc = curr.c + dc[i];
                        
                        // 맵 밖으로 나가면 무시
                        if (nr < 0 || nr >= length || nc < 0 || nc >= horizontal) continue;
                        if (visited[nr, nc]) continue;
                        
                        visited[nr, nc] = true;
                        
                        if (map[nr, nc] == NONE) {
                            // 빈칸이면 지게차가 이동할 수 있으므로 큐에 추가
                            q.Enqueue((nr, nc));
                        } 
                        else if (map[nr, nc] == target) {
                            // 타겟 컨테이너를 만났다면 (외부와 닿아있다는 뜻!) 
                            // 뺄 목록에 추가하고 큐에는 안 넣음 (뒤로 못 지나가니까)
                            toRemove.Add((nr, nc));
                        }
                    }
                }
                
                // BFS가 끝나고 찾은 것들을 한 번에 삭제
                foreach (var pos in toRemove) {
                    map[pos.r, pos.c] = NONE;
                    answer--;
                }
                
            } else { // 크레인 (전체 순회하며 무조건 삭제)
                for (int i = 1; i <= n; i++) {
                    for (int j = 1; j <= m; j++) {
                        if (map[i, j] == target) {
                            map[i, j] = NONE;
                            answer--;
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}