import java.io.*;
import java.util.*;

class Main {
    static int n;
    static ArrayList<int[]>[] graph;
    static int[] visited;

    public static void BFS(int start) {
        visited[start] = 0;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{visited[start], start});

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            int d = tmp[0];
            int cur = tmp[1];

            for (int[] edge : graph[cur]) {
                int next = edge[0];
                int w = edge[1];
                if (visited[next] == -1) {
                    visited[next] = d + w;
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
        }

        for (int i = 0; i <= n; i++) {
            visited[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            int u, v, w;
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            while (true) {
                v = Integer.parseInt(st.nextToken());
                if (v == -1) break;
                w = Integer.parseInt(st.nextToken());
                graph[u].add(new int[]{v, w});
                graph[v].add(new int[]{u, w});
            }
        }

        BFS(1);
        int farthest_node = 1;
        for (int i = 2; i <= n; i++) {
            farthest_node = visited[i] > visited[farthest_node] ? i : farthest_node;
        }

        for (int i = 0; i <= n; i++) {
            visited[i] = -1;
        }
        BFS(farthest_node);
        int r = visited[1];
        for (int i = 2; i <= n; i++) {
            r = r > visited[i] ? r : visited[i];
        }
        System.out.println(r);
    }
}