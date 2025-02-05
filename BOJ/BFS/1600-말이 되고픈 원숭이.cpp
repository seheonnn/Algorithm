// 백준 1600 말이 되고픈 원숭이 BFS
#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

#define MAX 201
using namespace std;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int hx[8] = { 1, 2, -1, -2, 1, 2, -1, -2 };
int hy[8] = { 2, 1, 2, 1, -2, -1, -2, -1 };

int k, w, h;
int graph[MAX][MAX];
int visited[MAX][MAX][31];

void BFS(int x, int y, int k) {
   deque<tuple<int, int, int>> queue;
   queue.push_back({ x, y, k });

   while (!queue.empty()) {
      auto [x, y, k] = queue.front();
      queue.pop_front();

      if (x == h - 1 and y == w - 1) {
          printf("%d\n", visited[h-1][w-1][k] - 1); // 1에서 시작했으므로 -1
          return;
      }

      for (int i = 0; i < 4; i++) {
          int nx = x + dx[i];
          int ny = y + dy[i];

          if (nx < 0 or h <= nx or ny < 0 or w <= ny) {
              continue;
          }

          if (graph[nx][ny] == 0 and visited[nx][ny][k] == 0) {
              visited[nx][ny][k] = visited[x][y][k] + 1;
              queue.push_back({nx, ny, k});
          }
      }
      if (k > 0) {
          for (int i = 0; i < 8; i++) {
              int nx = x + hx[i];
              int ny = y + hy[i];

              if (nx < 0 or h <= nx or ny < 0 or w <= ny) {
                  continue;
              }

              if (graph[nx][ny] == 0 and visited[nx][ny][k - 1] == 0) {
                  visited[nx][ny][k - 1] = visited[x][y][k] + 1;
                  queue.push_back({nx, ny, k - 1});
              }
          }
      }
   }
   printf("%d\n", -1); // 탈출 못하는 경우
}

int main() {
   scanf("%d", &k);
   scanf("%d %d", &w, &h);

   for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
         scanf("%d", &graph[i][j]);
      }
   }

   visited[0][0][k] = 1; // 1에서 시작
   BFS(0, 0, k);

   return 0;
}