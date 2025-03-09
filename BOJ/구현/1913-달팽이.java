import java.io.*;
import java.util.*;

public class Main {
    static int n, k, x1, y1;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        graph = new int[n][n];

        int x = 0;
        int y = 0;
        int nd = 0;
        for (int i = n * n; i > 0; i--) {
            graph[x][y] = i;

            if (graph[x][y] == k) {
                x1 = x + 1;
                y1 = y + 1;
            }
            int nx = x + dx[nd];
            int ny = y + dy[nd];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && graph[nx][ny] == 0) {
                x = nx;
                y = ny;
            } else {
                nd = (nd + 1) % 4;
                x = x + dx[nd];
                y = y + dy[nd];
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
        System.out.print(x1 + " " + y1 + "\n");
    }
}