// 백준 1260 DFS와 BFS
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#define MAX 1001
using namespace std;

vector<int> graph[MAX];
int visited[MAX];
int n, m, v;

void DFS(int v) {
   cout << v << " ";
   for (int cur : graph[v]) {
      if (visited[cur] == 0) {
         visited[cur] = 1;
         DFS(cur);
      }
   }
}

void BFS(int v) {
   deque<int> queue;
   queue.push_back(v);

   while (!queue.empty()) {
      v = queue.front();
      cout << v << " ";
      queue.pop_front();
      for (int cur : graph[v]) {
         if (visited[cur] == 0) {
            visited[cur] = 1;
            queue.push_back(cur);
         }
      }
   }
}

int main() {
   cin >> n >> m >> v;

   for (int i = 0; i < m; i++) {
      int u, v;
      cin >> u >> v;
      graph[u].push_back(v);
      graph[v].push_back(u);
   }

   for (int i = 0; i <= n; i++) {
      // 방문할 수 있는 정점이 여러 개인 경우 작은 것부터 방문하기 위해 정렬
      sort(graph[i].begin(), graph[i].end());
   }

   visited[v] = 1;
   DFS(v);
   cout << "\n";

   for (int i = 0; i <= n; i++)
      visited[i] = 0;

   visited[v] = 1;
   BFS(v);
   return 0;
}