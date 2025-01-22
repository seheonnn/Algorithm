//// 코드트리 트리 정점 거리 DFS
//#include <iostream>
//#include <deque>
//#include <vector>
//#define MAX 1001
//using namespace std;
//
//vector<pair<int, int>> graph[MAX];
//int visited[MAX];
//
//void DFS(int v, int dist) {
//    for (auto tmp : graph[v]) {
//        int cur = tmp.first;
//        int w = tmp.second;
//        if (visited[cur] == -1) {
//            visited[cur] = dist + w;
//            DFS(cur, visited[cur]);
//        }
//    }
//}
//
//int main() {
//    int n, m;
//    cin >> n >> m;
//
//    for (int i = 0; i < n - 1;i++) {
//        int u, v, w;
//        cin >> u >> v >> w;
//        graph[u].push_back({v, w});
//        graph[v].push_back({ u, w });
//    }
//
//    for (int i = 0; i < m; i++) {
//        for (int j = 0; j < n + 1; j++)
//            visited[j] = -1;
//        int s, e;
//        cin >> s >> e;
//
//        visited[s] = 0;
//        DFS(s, 0);
//        cout << visited[e] << "\n";
//    }
//    return 0;
//}

// 코드트리 트리 정점 거리 BFS
#include <iostream>
#include <vector>
#include <deque>

#define MAX 1001
using namespace std;

vector<pair<int, int>> graph[MAX];
int visited[MAX];

void BFS(int v, int dist) {
   deque<pair<int, int>> queue;
   queue.push_back({ v, dist });
   while (!queue.empty()) {
      int v = queue.front().first;
      int dist = queue.front().second;
      queue.pop_front(); // c++ deque의 front()는 실제로 제거하지 않음, pop_front()는 반환값 없음

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
   int n, m;
   cin >> n >> m;
   for (int i = 0; i < n - 1; i++) {
      int u, v, w;
      cin >> u >> v >> w;
      graph[u].push_back({ v, w });
      graph[v].push_back({ u, w });
   }

   for (int i = 0; i < m; i++) {
      for (int i = 0; i < n + 1; i++)
         visited[i] = -1;

      int s, e;
      cin >> s >> e;

      visited[s] = 0;
      BFS(s, 0);
      cout << visited[e] << "\n";
   }
   return 0;
}