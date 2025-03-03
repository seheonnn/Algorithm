import java.io.*;
import java.util.*;

public class Main {
    static int n, m, s, e;
    static ArrayList<int[]>[] graph;
    static int[] dist;
    static int[] prev;

    static ArrayList<Integer> r = new ArrayList<>();
    public static void Dijkstra(int v) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        dist[v] = 0;
        pq.add(new int[]{dist[v], v});

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
                    prev[next] = cur;
                    pq.add(new int[]{dist[next], next});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n + 1];
        dist = new int[n + 1];
        prev = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
            dist[i] = Integer.MAX_VALUE;
            prev[i] = -1;
        }

        for (int i = 0; i < m; i++) {
            int u, v, w;
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());

            graph[u].add(new int[]{v, w});
        }

        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        Dijkstra(s);
        System.out.println(dist[e]);

        List<Integer> path = new ArrayList<>();
        int node = e;
        while (node != -1) {
            path.add(node);
            node = prev[node];
        }
        Collections.reverse(path);

        System.out.println(path.size());
        for (int city : path) {
            System.out.print(city + " ");
        }
    }
}