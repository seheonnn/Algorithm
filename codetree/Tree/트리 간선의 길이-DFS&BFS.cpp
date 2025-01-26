
// 코드트리 트리 간선의 길이 DFS&BFS
#include <iostream>
#include <vector>
#include <deque>

#define MAX 10001

using namespace std;

vector<pair<int, int>> graph[MAX];
int visited[MAX];

void DFS(int v, int dist) {
   for (auto tmp : graph[v]) {
      int cur = tmp.first;
      int w = tmp.second;

      if (visited[cur] == -1) {
         visited[cur] = dist + w;
         DFS(cur, visited[cur]);
      }
   }
}

void BFS(int v, int dist) {
   deque<pair<int, int>> queue;
   queue.push_back({ v, dist });

   while (!queue.empty()) {
      int v = queue.front().first;
      int dist = queue.front().second;
      queue.pop_front();
      for (auto tmp : graph[v]) {
         int cur = tmp.first;
         int w = tmp.second;
         if (visited[cur] == -1) {
            visited[cur] = dist + w;
            queue.push_back({ cur, visited[cur] });
         }
      }
   }
}

int main() {
   int n;
   cin >> n;

   for (int i = 0; i < n; i++) {
      int u, v, w;
      cin >> u >> v >> w;
      graph[u].push_back({ v, w });
      graph[v].push_back({ u, w });
   }

   for (int i = 0; i < n + 1; i++) {
      visited[i] = -1;
   }
   visited[1] = 0;
   BFS(1, 0);
   int farthest_node = 1;
   for (int i = 2; i <= n; i++) {
      if (visited[i] > visited[farthest_node])
         farthest_node = i;
   }

   for (int i = 0; i < n + 1; i++) {
      visited[i] = -1;
   }
   visited[farthest_node] = 0;
   DFS(farthest_node, 0);
   farthest_node = 1;
   for (int i = 2; i <= n; i++) {
      if (visited[i] > visited[farthest_node])
         farthest_node = i;
   }

   cout << visited[farthest_node] << "\n";
}