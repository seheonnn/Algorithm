// 프로그래머스 네트워크 BFS

// import java.util.*;

// class Solution {
//     static ArrayList<Integer>[] graph;
//     static int[] visited;
//     public static void BFS(int n, int v) {
//         Queue<Integer> queue = new LinkedList<>();
//         queue.add(v);

//         while(!queue.isEmpty()) {
//             int cur = queue.poll();
//             for (int next : graph[cur]) {
//                 if (visited[next] == 0) {
//                     visited[next] = 1;
//                     queue.add(next);
//                 }
//             }
//         }

//     }

//     public int solution(int n, int[][] computers) {
//         int answer = 0;
//         graph = new ArrayList[n + 1];
//         visited = new int[n + 1];
//         for (int i = 0; i <= n; i++) {
//             graph[i] = new ArrayList<>();
//         }

//         for (int i = 0; i < n; i++) {
//             for (int j = 0; j < n; j++) {
//                if (computers[i][j] == 1) {
//                    graph[i].add(j);
//                }
//             }
//         }

//         for (int i = 0; i < n; i++) {
//             if (visited[i] == 0) {
//                 visited[i] = 1;
//                 BFS(n, i);
//                 answer++;
//             }
//         }

//         return answer;
//     }
// }

// 프로그래머스 네트워크 DFS

import java.util.*;

class Solution {
    static int[] visited;
    public static void BFS(int n, int[][] computers, int v) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);

        while(!queue.isEmpty()) {
            int cur = queue.poll();
            for (int next = 0; next < n; next++) {
                if (computers[cur][next] == 1 && visited[next] == 0) {
                    visited[next] = 1;
                    queue.add(next);
                }
            }
        }
    }

    public static void DFS(int n, int[][] computers, int v) {
        for (int next = 0; next < n; next++) {
            if (computers[v][next] == 1 && visited[next] == 0) {
                visited[next] = 1;
                DFS(n, computers, next);
            }
        }
    }

    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new int[n];
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                // BFS(n, computers, i);
                DFS(n, computers, i);
                answer++;
            }
        }
        return answer;
    }
}