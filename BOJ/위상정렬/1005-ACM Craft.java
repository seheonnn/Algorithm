import java.util.*;
import java.io.*;

class Main {
    static int tc, n, k, w;
    static ArrayList<Integer>[] graph;
    static int[] inDegree;
    static int[] times;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        tc = Integer.parseInt(st.nextToken());
        for (int t = 0; t < tc; t++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            graph = new ArrayList[n + 1];
            times = new int[n + 1];
            inDegree = new int[n + 1];
            dp = new int[n + 1];

            for (int i = 1; i <= n; i++) {
                graph[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                times[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 1; i <= k; i++) {
                st = new StringTokenizer(br.readLine());
                int x, y;
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                graph[x].add(y);
                inDegree[y]++;
            }
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());

            PriorityQueue<Integer> pq = new PriorityQueue<>();
            for (int i = 1; i <= n; i++) {
                if (inDegree[i] == 0) {
                    pq.add(i);
                    dp[i] = times[i];
                }
            }

            while(!pq.isEmpty()) {
                int cur = pq.poll();
                for (int next : graph[cur]) {
                    dp[next] = Math.max(dp[next], dp[cur] + times[next]);
                    inDegree[next]--;

                    if (inDegree[next] == 0) {
                        pq.add(next);
                    }
                }
            }

            System.out.println(dp[w]);
        }
    }
}
