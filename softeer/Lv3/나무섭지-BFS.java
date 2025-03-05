// 소프티어 나무섭지 BFS

import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static char[][] graph;
    static int[][] timeNam;
    static int[][] timeGho;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    static int d1 = -1;
    static int d2 = -1;
    static void BfsNam(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            x = tmp[0];
            y = tmp[1];

            if (graph[x][y] == 'D') {
                d1 = x;
                d2 = y;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || n <= nx || ny < 0 || m <= ny) continue;
                if ((graph[nx][ny] == '.' || graph[nx][ny] == 'D') && timeNam[nx][ny] == 0) {
                    timeNam[nx][ny] = timeNam[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }

    static void BfsGho() {
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 'G') {
                    timeGho[i][j] = 1;
                    queue.add(new int[]{i, j});
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
                if (timeGho[nx][ny] == 0) {
                    timeGho[nx][ny] = timeGho[x][y] + 1;
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
        graph = new char[n][m];
        timeNam = new int[n][m];
        timeGho = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            for (int j = 0; j < m; j++) {
               graph[i][j] = str.charAt(j);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 'N') {
                    timeNam[i][j] = 1;
                    BfsNam(i, j);
                }
            }
        }

        BfsGho();

        boolean isPoss = false;
        if (d1 != -1 && d2 != -1) {
            if (timeNam[d1][d2] < timeGho[d1][d2] || timeGho[d1][d2] == 0) isPoss = true;
        }
        System.out.println(isPoss ? "Yes" : "No");
    }
}