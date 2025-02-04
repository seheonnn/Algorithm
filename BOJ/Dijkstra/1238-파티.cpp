// 백준 1238 파티 다익스트라
#include <iostream>
#include <vector>
#include <deque>
#include <climits>
#define MAX 1001
using namespace std;

int n, m, x;
vector<vector<pair<int, int>>> graph;
vector<vector<pair<int, int>>> graph_reverse;
int dist_from_x[MAX];
int dist_to_x[MAX];

void Dijkstra(vector<vector<pair<int, int>>>& graph, int v, int dist_arr[]) {
   for (int i = 1; i <= n; i++) {
      dist_arr[i] = INT_MAX; // 초기화
   }

   deque<pair<int, int>> queue;
   dist_arr[v] = 0;
   queue.push_back({ v, 0 });

   while (!queue.empty()) {
      int cur = queue.front().first;
      int dist = queue.front().second;
      queue.pop_front();

      if (dist > dist_arr[cur]) continue;
      for (auto edge : graph[cur]) {
         int next = edge.first;
         int w = edge.second;
         int new_dist = dist + w;

         if (new_dist < dist_arr[next]) {
            dist_arr[next] = new_dist;
            queue.push_back({ next, new_dist });
         }
      }
   }
}

int main() {
   scanf("%d %d %d", &n, &m, &x);
   graph.resize(n + 1);
   graph_reverse.resize(n + 1);

   for (int i = 0; i < m; i++) {
      int u, v, w;
      scanf("%d %d %d", &u, &v, &w);
      graph[u].push_back({ v, w });
      graph_reverse[v].push_back({ u, w });
   }
   // x에서 각각의 마을로 가는 거리 계산
   Dijstra(graph, x, dist_from_x);
   // 각각의 마을에서 x로 가는 거리 계산
   Dijstra(graph_reverse, x, dist_to_x);

   int r = 0;
   for (int i = 1; i <= n; i++) {
      r = max(r, dist_from_x[i] + dist_to_x[i]);
   }

   printf("%d\n", r);

   return 0;
}