import java.util.*;
import java.io.*;

class Main {
    static int tc, m, n, k;
    static int[][] graph;
    static int[][] visited;

    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};

    public static void BFS(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        visited[x][y] = 1;
        queue.add(new int[]{x, y});

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            x = tmp[0];
            y = tmp[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || n <= nx || ny < 0 || m <= ny) continue;

                if (graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                    visited[nx][ny] = 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        tc = Integer.parseInt(st.nextToken());

        for (int t = 0; t < tc; t++) {
            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            graph = new int[n + 1][m + 1];
            visited = new int[n + 1][m + 1];

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph[y][x] = 1;
            }

            int cnt = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (graph[i][j] == 1 && visited[i][j] == 0) {
                        cnt += 1;
                        BFS(i, j);
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}