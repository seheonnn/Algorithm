import java.util.*;
import java.io.*;

class Solution {

    static ArrayList<int[]>[] graph;
    static int[] dist;
    public void Dijkstra(int start) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        dist[start] = 0;
        pq.add(new int[]{dist[start], start});

        while (!pq.isEmpty()) {
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
                    pq.add(new int[]{new_dist, next});
                }
            }
        }
    }

    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        graph = new ArrayList[n + 1];
        dist = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        Arrays.fill(dist, Integer.MAX_VALUE);

        for (int[] tmp : roads) {
            int u = tmp[0], v = tmp[1];
            graph[u].add(new int[] {v, 1});
            graph[v].add(new int[] {u, 1});
        }

        Dijkstra(destination);

        for (int i = 0; i < sources.length; i++) {
            answer[i] = (dist[sources[i]] == Integer.MAX_VALUE ? -1 : dist[sources[i]]);
        }
        return answer;
    }
}


// import java.util.*;
// import java.io.*;

// class Solution {

//     static ArrayList<Integer>[] graph;
//     static int[] dist;
//     public void Dijkstra(int start) {
//         PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
//         dist[start] = 0;
//         pq.add(new int[]{dist[start], start});

//         while (!pq.isEmpty()) {
//             int[] tmp = pq.poll();
//             int d = tmp[0];
//             int cur = tmp[1];

//             if (d > dist[cur]) continue;

//             for (int next : graph[cur]) {
//                 int new_dist = d + 1;
//                 if (new_dist < dist[next]) {
//                     dist[next] = new_dist;
//                     pq.add(new int[]{new_dist, next});
//                 }
//             }
//         }
//     }

//     public int[] solution(int n, int[][] roads, int[] sources, int destination) {
//         int[] answer = new int[sources.length];
//         graph = new ArrayList[n + 1];
//         dist = new int[n + 1];

//         for (int i = 0; i <= n; i++) {
//             graph[i] = new ArrayList<>();
//         }

//         Arrays.fill(dist, Integer.MAX_VALUE);

//         for (int[] tmp : roads) {
//             int u = tmp[0], v = tmp[1];
//             graph[u].add(v);
//             graph[v].add(u);
//         }

//         Dijkstra(destination);

//         for (int i = 0; i < sources.length; i++) {
//             answer[i] = (dist[sources[i]] == Integer.MAX_VALUE ? -1 : dist[sources[i]]);
//         }
//         return answer;
//     }
// }