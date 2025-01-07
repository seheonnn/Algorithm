// 백준 1913 - 달팽이
#include <iostream>

#define MAX 999

using namespace std;

int dx[4] = {1,  0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int nd = 0;
int graph[MAX][MAX];

int main() {
   int n, k;
   int a, b; // k의 좌표 저장
   a = 0;
   b = 0;
   cin >> n >> k;

   for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
         graph[i][j] = 0;
      }
   }

   int x = 0;
   int y = 0;
   for (int i = n * n; i > 0; i--) {
      if (i == k) {
         a = x + 1;
         b = y + 1;
      }
      graph[x][y] = i;
      int nx = x + dx[nd];
      int ny = y + dy[nd];
      if (0 <= nx and nx < n and 0 <= ny and ny < n and graph[nx][ny] == 0) {
         x = nx;
         y = ny;
      }
      else {
         nd = (nd + 1) % 4;
         x = x + dx[nd];
         y = y + dy[nd];
      }
   }

   for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
         cout << graph[i][j] << " ";
      }
      cout << "\n";
   }
   cout << a << " " << b;
   return 0;
}
