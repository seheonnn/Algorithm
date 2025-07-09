import java.util.*;
import java.io.*;

class Main {
    static ArrayList<Integer>[] graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];
        int[] inDegree = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x].add(y);
            inDegree[y]++;
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 1; i <= n; i++) {
            if (inDegree[i] == 0) {
                pq.add(i);
            }
        }

        StringBuilder sb = new StringBuilder();

        while (!pq.isEmpty()) {
            int cur = pq.poll();
            sb.append(cur).append(" ");

            for (int next : graph[cur]) {
                inDegree[next]--;
                if (inDegree[next] == 0) {
                    pq.add(next);
                }
            }
        }

        System.out.println(sb.toString().trim());
    }
}