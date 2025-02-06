// 소프티어 나무 섭지 BFS
#include <iostream>
#include <deque>
#define MAX 1000
using namespace std;

int n, m;
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };
char graph[MAX][MAX]; // 입력받은 그래프
int visited[MAX][MAX]; // 남우 방문 시간

int ghost_time[MAX][MAX]; // 유령 방문 시간

int poss = false;

void BFS_ghost() {
   deque<pair<int, int>> queue;

   for (int i = 0;i < n;i++) {
      for (int j = 0; j < m;j++) {
         if (graph[i][j] == 'G') {
            queue.push_back({ i, j });
            ghost_time[i][j] = 1;
         }
      }
   }

   while (!queue.empty()) {
      int x = queue.front().first;
      int y = queue.front().second;
      queue.pop_front();
      for (int i = 0; i < 4; i++) {
         int nx = x + dx[i];
         int ny = y + dy[i];
         if (nx < 0 or n <= nx or ny < 0 or m <= ny)
            continue;
         if (ghost_time[nx][ny] == 0) {
            ghost_time[nx][ny] = ghost_time[x][y] + 1;
            queue.push_back({ nx, ny });
         }
      }
   }
}

void BFS_nam(int x, int y) {
   deque<pair<int, int>> queue;
   queue.push_back({ x, y });

   while (!queue.empty()) {
      int x = queue.front().first;
      int y = queue.front().second;
      queue.pop_front();

      for (int i = 0; i < 4; i++) {
         int nx = x + dx[i];
         int ny = y + dy[i];

         if (nx < 0 or n <= nx or ny < 0 or m <= ny)
            continue;
         if (visited[nx][ny] == 0 and graph[nx][ny] != '#') {
            visited[nx][ny] = visited[x][y] + 1;
            queue.push_back({ nx, ny });
         }
         if (graph[nx][ny] == 'D') {
            // 탈출구에 유령이 도달하지 못하거나 남우보다 먼저 도달한 것이 아니라면 탈출 성공
            if (ghost_time[nx][ny] == 0 or visited[nx][ny] < ghost_time[nx][ny]) {
               poss = true;
            }
         }
      }
   }
}

int main() {


   cin >> n >> m;
   for (int i = 0;i < n;i++) {
      for (int j = 0; j < m;j++) {
         cin >> graph[i][j];
      }
   }
   BFS_ghost();
   for (int i = 0;i < n;i++) {
      for (int j = 0; j < m;j++) {
         if (graph[i][j] == 'N') {
            visited[i][j] = 1;
            BFS_nam(i, j);
         }
      }
   }

   if (poss)
      cout << "Yes\n";
   else
      cout << "No\n";
   return 0;
}
