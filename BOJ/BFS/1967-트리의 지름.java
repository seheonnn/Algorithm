import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static ArrayList<int[]>[] graph;
    static int[] visited;

    static void BFS(int v, int dist) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{dist, v});

        while (!queue.isEmpty()) {
            int[] tmp = queue.poll();
            int d = tmp[0];
            int cur = tmp[1];

            for (int[] edge : graph[cur]) {
                int next = edge[0];
                int w = edge[1];
                int new_dist = d + w;
                if (visited[next] == -1) {
                    visited[next] = new_dist;
                    queue.add(new int[]{visited[next], next});
                }

            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        visited = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
            visited[i] = -1;
        }

        for (int i = 0; i < n - 1; i++) {
            int u, v, w;
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        visited[1] = 0;
        BFS(1, visited[1]);
        int farthest_node = 1;
        for (int i = 2; i <= n; i++) {
            farthest_node = visited[farthest_node] > visited[i] ? farthest_node : i;
        }

        for (int i = 0; i <= n; i++) {
            visited[i] = -1;
        }
        visited[farthest_node] = 0;
        BFS(farthest_node, visited[farthest_node]);
        int r = 0;
        for (int i = 1; i <= n; i++) {
            r = Math.max(r, visited[i]);
        }
        System.out.println(r);
    }
}