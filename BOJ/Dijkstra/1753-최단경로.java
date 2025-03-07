import java.io.*;
import java.util.*;

public class Main {
    static int v, e, k;
    static ArrayList<int[]>[] graph;
    static int[] dist;

    static void Dijkstra(int start) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        dist[start] = 0;
        pq.add(new int[]{dist[start], start});

        while(!pq.isEmpty()) {
            int[] tmp = pq.poll();
            int d = tmp[0];
            int cur = tmp[1];

            if (d > dist[cur]) continue;
            for (int[] edge : graph[cur]) {
                int next = edge[0];
                int w = edge[1];
                int new_dist = w + d;
                if (new_dist < dist[next]) {
                    dist[next] = new_dist;
                    pq.add(new int[]{dist[next], next});
                }
            }
        }
    }
    public static void main(String[] atgs) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        graph = new ArrayList[v + 1];
        dist = new int[v + 1];
        for (int i = 0; i<= v;i++) {
            graph[i] = new ArrayList<>();
            dist[i] = Integer.MAX_VALUE;
        }

        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < e; i++) {
            int u, v, w;
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[]{v, w});
        }

        Dijkstra(k);
        for (int i = 1; i <= v; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(dist[i]);
            }
        }
    }
}