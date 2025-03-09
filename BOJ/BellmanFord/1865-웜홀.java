// 백준 1865 웜홀 벨만포드
import java.io.*;
import java.util.*;

public class Main {
    static int tc;
    static ArrayList<int[]>[] graph;
    static int[] dist;

    static boolean BellmanFord(int start, int n) {
        dist[start] = 0;

        // (N-1)번 반복하여 최단 거리 계산
        for (int i = 1; i < n; i++) {
            for (int cur = 1; cur <= n; cur++) {
                for (int[] edge : graph[cur]) {
                    int next = edge[0];
                    int w = edge[1];
                    if (dist[cur] != Integer.MAX_VALUE && dist[next] > dist[cur] + w) {
                        dist[next] = dist[cur] + w;
                    }
                }
            }
        }

        // 한 번 더 돌려서 음수 사이클 존재 여부 확인
        for (int cur = 1; cur <= n; cur++) {
            for (int[] edge : graph[cur]) {
                int next = edge[0];
                int w = edge[1];
                if (dist[cur] != Integer.MAX_VALUE && dist[next] > dist[cur] + w) {
                    return true; // 음수 사이클 발견
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        tc = Integer.parseInt(st.nextToken());

        for (int t = 0; t < tc; t++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph = new ArrayList[n + 1];
            dist = new int[n + 1];
            for (int i = 0; i <= n; i++) {
                graph[i] = new ArrayList<>();
                dist[i] = Integer.MAX_VALUE;
            }

            // 도로 입력 (양방향)
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int g = Integer.parseInt(st.nextToken());
                graph[u].add(new int[]{v, g});
                graph[v].add(new int[]{u, g});
            }

            // 웜홀 입력 (단방향, 음수 가중치)
            for (int i = 0; i < w; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int g = Integer.parseInt(st.nextToken());
                graph[u].add(new int[]{v, -g});
            }

            boolean r = false;

            for (int i = 1; i <= n; i++) {
                if (dist[i] == Integer.MAX_VALUE) { // 아직 방문하지 않은 컴포넌트에 대해 실행
                    if (BellmanFord(i, n)) {
                        r = true;
                        break;
                    }
                }
            }

            System.out.println(r ? "YES" : "NO");
        }
    }
}
