// 프로그래머스 합승 택시 요금

import java.io.*;
import java.util.*;

class Solution {
    ArrayList<int[]>[] graph;

    public void Dijkstra(int start, int[] dist) {
        Arrays.fill(dist, Integer.MAX_VALUE);
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
                if (dist[next] >= new_dist) {
                    dist[next] = new_dist;
                    pq.add(new int[] {dist[next], next});
                }
            }
        }
    }

    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        graph = new ArrayList[n + 1];

        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] tmp : fares) {
            int u = tmp[0], v = tmp[1], w = tmp[2];
            graph[u].add(new int[]{v, w});
            graph[v].add(new int[]{u, w});
        }

        int[] fromS = new int[n + 1];;
        int[] fromA = new int[n + 1];;
        int[] fromB = new int[n + 1];;

        Dijkstra(s, fromS);
        Dijkstra(a, fromA);
        Dijkstra(b, fromB);

        for (int i = 1; i <= n; i++) {
            if (fromS[i] != Integer.MAX_VALUE && fromA[i] != Integer.MAX_VALUE && fromB[i] != Integer.MAX_VALUE) {
                answer = Math.min(answer, fromS[i] + fromA[i] + fromB[i]);
            }
        }

        return answer;
    }
}