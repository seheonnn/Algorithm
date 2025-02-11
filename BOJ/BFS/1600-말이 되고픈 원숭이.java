// 백준 1600 말이 되고픈 원숭이 BFS

import java.io.*;
import java.util.*;

public class Main {
    static int k, w, h;
    static int[][] graph;
    static int[][][] visited;
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {-1, 0, 1, 0};
    static int[] hx = {2, 2, 1, -1, -2, -2, -1, 1};
    static int[] hy = {1, -1, -2, -2, -1, 1, 2, 2};

    public static void BFS(int x, int y, int k) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y, k});

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            x = tmp[0];
            y = tmp[1];
            k = tmp[2];

            if (x == h - 1 && y == w - 1) {
                System.out.println(visited[h - 1][w - 1][k] - 1); // 1 시작이므로 -1
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || h <= nx || ny < 0 || w <= ny) continue;
                if (visited[nx][ny][k] == 0 && graph[nx][ny] == 0) {
                    visited[nx][ny][k] = visited[x][y][k] + 1;
                    queue.add(new int[]{nx, ny, k});
                }
            }
            if (k > 0) {
                for (int i = 0; i < 8; i++) {
                    int nhx = x + hx[i];
                    int nhy = y + hy[i];

                    if (nhx < 0 || h <= nhx || nhy < 0 || w <= nhy) continue;
                    if (visited[nhx][nhy][k - 1] == 0 && graph[nhx][nhy] == 0) {
                        visited[nhx][nhy][k - 1] = visited[x][y][k] + 1;
                        queue.add(new int[]{nhx, nhy, k - 1});
                    }
                }
            }
        }
        System.out.println(-1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        graph = new int[h][w];
        visited = new int[h][w][k + 1];

        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited[0][0][k] = 1;
        BFS(0, 0, k);
    }
}