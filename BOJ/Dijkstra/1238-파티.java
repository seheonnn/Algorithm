// 백준 1238 파티 다익스트라

import java.io.*;
import java.util.*;

public class Main {
    static int n, m, x;
    static ArrayList<int[]>[] graph;
    static ArrayList<int[]>[] graph_reverse;
    static int[] dist_from_x;
    static int[] dist_to_x;

    static void Dijkstra(ArrayList<int[]>[] arr, int v, int[] dist_arr) {
        for (int i = 1; i <= n; i++) {
            dist_arr[i] = Integer.MAX_VALUE;
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a->a[0]));
        dist_arr[v] = 0;
        pq.add(new int[]{dist_arr[v], v});

        while(!pq.isEmpty()) {
            int[] tmp = pq.poll();
            int d = tmp[0];
            int cur = tmp[1];

            if (d > dist_arr[cur]) continue;

            for (int[] edge : arr[cur]) {
                int next = edge[0];
                int w = edge[1];
                int new_dist = w + d;
                if (new_dist < dist_arr[next]) {
                    dist_arr[next] = new_dist;
                    pq.add(new int[]{dist_arr[next], next});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];
        graph_reverse = new ArrayList[n + 1];
        dist_from_x = new int[n + 1];
        dist_to_x = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
            graph_reverse[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u, v, w;
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[]{v, w});
            graph_reverse[v].add(new int[]{u, w});
        }

        // x에서 각각의 마을로 가는거리 계산
        Dijkstra(graph, x, dist_from_x);
        // 각각의 마을에서 x로 가는 거리 계산
        Dijkstra(graph_reverse, x, dist_to_x);

        int r = 0;
        for (int i = 1; i <= n; i++) {
            r = Math.max(r, dist_from_x[i] + dist_to_x[i]);
        }

        System.out.println(r);
    }
}