import java.io.*;
import java.util.*;

public class Main {
    static int m, n;
    static int[][] graph;
    static int[][] visited;
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};
    static void BFS() {
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1) {
                    queue.add(new int[]{i, j});
                    visited[i][j] = 1;
                }
            }
        }

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            int x = tmp[0];
            int y = tmp[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || n <= nx || ny < 0 || m <= ny) continue;
                if (graph[nx][ny] == 0 && visited[nx][ny] == 0) {
                    visited[nx][ny] = 1;
                    graph[nx][ny] = graph[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        BFS();
        int r = 0;
        boolean poss = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                r = Math.max(r, graph[i][j]);
                if (graph[i][j] == 0) {
                    poss = false;
                }
            }
        }

        if (poss) {
            System.out.println(r - 1); // 1로 시작하므로
        } else {
            System.out.println(-1);
        }

    }
}