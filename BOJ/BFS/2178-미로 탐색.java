// 백준 2178 미로 탐색 BFS

import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[][] graph;
    static int[][] visited;
    static String str;
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};

    public static void BFS(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            x = tmp[0];
            y = tmp[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || n <= nx || ny < 0 || m <= ny) continue;
                if (visited[nx][ny] == 0 && graph[nx][ny] == 1) {
                    visited[nx][ny] = visited[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            str = st.nextToken();
            for (int j = 0; j < m; j++) {
                graph[i][j] = str.charAt(j) - '0';
            }
        }

        visited[0][0] = 1;
        BFS(0, 0);

        System.out.println(visited[n - 1][m - 1]);
    }
}