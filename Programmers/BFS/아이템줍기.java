// 프로그래머스 Lv3 아이템 줍기

import java.util.*;
class Solution {
    static int answer = 0;
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};
    static int[][] graph;
    static int[][] visited;
    public static void BFS(int x, int y, int ix, int iy) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            x = tmp[0];
            y = tmp[1];

            if (x == (ix) && y == (iy)) {
                answer = visited[ix][iy] / 2;
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || 102 <= nx || ny < 0 || 102 <= ny) continue;
                if (graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                    visited[nx][ny] = visited[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        graph = new int[102][102];
        visited = new int[102][102];

        for (int i = 0; i <= 101; i++) {
            for (int j = 0; j <= 101; j++) {
                graph[i][j] = -1;
            }
        }

        for (int[] lst : rectangle) {
            int x1 = lst[0] * 2;
            int y1 = lst[1] * 2;
            int x2 = lst[2] * 2;
            int y2 = lst[3] * 2;

            // 테두리와 내부 영역 구분 주의 !
            for (int i = x1; i <= x2; i++) {
                for (int j = y1; j <= y2; j++) {
                    if (x1 < i && i < x2 && y1 < j && j < y2) {
                        graph[i][j] = 0; // 내부 영역은 0으로 만듦
                    } else if (graph[i][j] != 0) {
                        graph[i][j] = 1; // 테두리 유지
                    }
                }
            }
        }

        visited[characterX * 2][characterY * 2] = 0;
        BFS(characterX * 2, characterY * 2, itemX * 2, itemY * 2);

        return answer;
    }
}