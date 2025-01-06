#include <iostream>
#define MAX 50
using namespace std;

int t;
int m, n, k;
int dx[4] = {0, -1, 0, 1};
int dy[4] = { -1, 0, 1, 0 };
int graph[MAX][MAX];
int visited[MAX][MAX];

void dfs(int x, int y) {
   for (int i = 0;i < 4;i++) {
      int nx, ny;
      nx = x + dx[i];
      ny = y + dy[i];
      if (nx < 0 or m <= nx or ny < 0 or n <= ny)
         continue;
      if (graph[nx][ny] == 1 and visited[nx][ny] == 0) {
         visited[nx][ny] = 1;
         dfs(nx, ny);
      }
   }
}

int main() {
   cin >> t;
   for (int a = 0; a < t; a++) {
      cin >> m >> n >> k;

      for (int i = 0;i < m;i++) {
         for (int j = 0;j < n;j++) {
            graph[i][j] = 0;
            visited[i][j] = 0;
         }
      }

      for (int i = 0;i < k;i++) {
         int x, y;
         cin >> x >> y;
         graph[x][y] = 1;
      }

      int cnt = 0;

      for (int i = 0;i < m;i++) {
         for (int j = 0;j < n; j++) {
            if (graph[i][j] == 1 and visited[i][j] == 0) {
               visited[i][j] = 1;
               dfs(i, j);
               cnt++;
            }
         }
      }
      cout << cnt << "\n";
   }
   return 0;
}