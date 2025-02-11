import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    // static int[][] graph;
    static long[][] graph;

    public static void FloydWarshall() {
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (graph[i][j] > graph[i][k] + graph[k][j]) {
                        graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == j) {
                    graph[i][j] = 0; // 자기 자신과의 거리는 0
                } else {
                    // 플로이드 와샬에선 Integer.MAX_VALUE 사용하면 정수 오버플로우 발생함
                    // long 이나 (Integer.MAX_VALUE) / 2 사용할 것
                    graph[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            int a, b;
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        FloydWarshall();
        int r = 0;
        int min = Integer.MAX_VALUE;

        for (int i = 1; i <= n; i++) {
            int tmp = 0;
            for (int j = 1; j <= n; j++) {
                tmp += graph[i][j];
            }
            if (min > tmp) {
                min = tmp;
                r = i;
            }
        }

        System.out.println(r);
    }
}