// 백준 7576 토마토 BFS
#include <iostream>
#include <deque>
#include <algorithm>
#define MAX 1000
using namespace std;

int graph[MAX][MAX];
int visited[MAX][MAX];
int n, m;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

void BFS() {
   deque <pair<int, int>> queue;
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < m;j++) {
         if (graph[i][j] == 1) {
            queue.push_back({ i, j });
            visited[i][j] = 1;
         }
      }
   }

   while (!queue.empty()) {
      int x = queue.front().first;
      int y = queue.front().second;
      queue.pop_front();
      for (int i = 0; i < 4;i++) {
         int nx = x + dx[i];
         int ny = y + dy[i];
         if (nx < 0 or n <= nx or ny < 0 or m <= ny)
            continue;
         if (graph[nx][ny] == 0 and visited[nx][ny] == 0) {
            visited[nx][ny] = 1;
            graph[nx][ny] = graph[x][y] + 1;
            queue.push_back({ nx, ny });
         }
      }
   }
}

int main() {
   cin >> m >> n;

   for (int i = 0; i < n; i++) {
      for (int j = 0; j < m;j++) {
         cin >> graph[i][j];
      }
   }

   BFS();

   int r = -MAX;
   int flag = true; // 토마토가 모두 익을 수 있는지
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < m;j++) {
         if (graph[i][j] == 0)
            flag = false;
         r = max(r, graph[i][j]);
      }
   }

   if (flag)
      cout << r - 1 << "\n";
   else
      cout << -1 << "\n";

   return 0;
}