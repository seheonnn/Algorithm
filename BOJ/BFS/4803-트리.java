import java.util.*;
import java.io.*;

class Main {

    static int n, m;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static boolean BFS(int start) {
        Queue<int[]> queue = new LinkedList<>();
        visited[start] = true;
        queue.add(new int[]{start, 0}); // 현재 노드, 부모 노드

        while(!queue.isEmpty()) {
            int[] tmp = queue.poll();
            int cur = tmp[0];
            int parent = tmp[1];

            for (int next : graph[cur]) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.add(new int[]{next, cur});
                }
                // 이미 방문한 노드일 때
                else if (next != parent) { // 다음 노드가 이미 방문했던 부모 노드가 아니라면 사이클임
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int caseNum = 1;
        while(true) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            if (n == 0 && m == 0) break;

            graph = new ArrayList[n + 1];
            visited = new boolean[n + 1];
            for (int i = 0; i <= n ;i++) {
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph[a].add(b);
                graph[b].add(a);
            }

            int cnt = 0;
            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    if (BFS(i)) {
                        cnt++;
                    }
                }
            }
            if (cnt == 0)
                System.out.printf("Case %d: No trees.\n", caseNum);
            else if (cnt == 1)
                System.out.printf("Case %d: There is one tree.\n", caseNum);
            else
                System.out.printf("Case %d: A forest of %d trees.\n", caseNum, cnt);

            caseNum++;
        }
    }
}