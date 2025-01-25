// 백준 1167 트리의 지름 BFS
#include <iostream>
#include <vector>
#include <deque>
#define MAX 100001

using namespace std;

int n;
vector<vector<pair<int, int>>> graph;
int visited[MAX];

void BFS(int v, int dist) {
   deque<pair<int, int>> queue;
   queue.push_back({ v, dist });
   while (!queue.empty()) {
      v = queue.front().first;
      dist = queue.front().second;
      queue.pop_front();
      for (auto edge : graph[v]) {
         int cur = edge.first;
         int w = edge.second;
         if (visited[cur] == -1) {
            visited[cur] = dist + w;
            queue.push_back({ cur, visited[cur] });
         }
      }
   }
}

int main() {
   scanf("%d", &n);

   graph.resize(n + 1); // resize 해주어야 !

   for (int i = 0; i <= n; i++) {
      visited[i] = -1;
   }

   for (int i = 0; i < n; i++) {
      int u, v, w;
      scanf("%d", &u);

      while (true) {
         scanf("%d", &v);
         if (v == -1)
            break;

         scanf("%d", &w);
         graph[u].push_back({ v, w });
         graph[v].push_back({ u, w });
      }
   }

   visited[1] = 0;
   BFS(1, 0);
   int farthest_node = 1;
   for (int i = 2; i <= n; i++) {
      farthest_node = visited[i] > visited[farthest_node] ? i : farthest_node;
   }

   // visited 초기화
   for (int i = 0; i <= n; i++) {
      visited[i] = -1;
   }
   visited[farthest_node] = 0;
   BFS(farthest_node, 0);
   int r = 0;
   for (int i = 1; i <= n; i++) {
      r = visited[i] > r ? visited[i] : r;
   }

   printf("%d\n", r);

   return 0;
}