// 1167 트리의 지름 BFS

import java.io.*;
import java.util.*;

public class Main {
    static List<int[]>[] graph;
    static int[] visited;
    static int n;

    static void BFS(int v, int dist) {
         Queue<int[]> queue = new LinkedList<>();
         queue.add(new int[]{dist, v});

         while (!queue.isEmpty()) {
             int[] tmp = queue.poll();
             dist = tmp[0];
             v = tmp[1];

             for (int[] edge : graph[v]) {
                 // graph에서 가져옴 !! queue랑 헷갈리지 않기 !
                 int next = edge[0];
                 int w = edge[1];

                 if (visited[next] == -1) {
                     visited[next] = dist + w;
                     queue.add(new int[] {visited[next], next});
                 }
             }
         }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        visited = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i <= n; i++) {
            visited[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            int u, v, w;
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            while(true) {
                v = Integer.parseInt(st.nextToken());
                if (v == -1) {
                    break;
                }
                w = Integer.parseInt(st.nextToken());
                graph[u].add(new int[]{v, w});
                graph[v].add(new int[]{u, w});
            }
        }

        visited[1] = 0;
        BFS(1, visited[1]);
        int farthest_node = 1;
        for (int i = 2; i <= n; i++) {
            farthest_node = visited[i] > visited[farthest_node] ? i : farthest_node;
        }

        for (int i = 1; i <= n; i++) {
            visited[i] = -1;
        }
        visited[farthest_node] = 0;
        BFS(farthest_node, visited[farthest_node]);

        int r = -1;
        for (int i = 1; i <= n; i++) {
            r = visited[i] > r ? visited[i] : r;
        }
        System.out.println(r);

    }
}