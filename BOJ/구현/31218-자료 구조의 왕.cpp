// 백준 31218 자료 구조의 왕 구현
#include <iostream>
#define MAX 1001

using namespace std;

int n, m, q;
int ground[MAX][MAX]; // 잔디가 있음 : 0 / 잔디가 없음 : 1

int cnt;

int main() {
   scanf("%d %d %d", &n, &m, &q);

   cnt = n * m;

   for (int i = 0; i < q; i++) {
      int qNum;
      scanf("%d", &qNum);

      if (qNum == 1) {
         int dy, dx, y, x;
         scanf("%d %d %d %d", &dy, &dx, &y, &x);
         y--;
         x--;
         while (true) {
            if (ground[y][x] == 1)
               break;
            ground[y][x] = 1;
            cnt--;

            int ny = y + dy;
            int nx = x + dx;
            if (ny < 0 or ny >= n or nx < 0 or nx >= m)
               break;
            y = y + dy;
            x = x + dx;
         }
      }

      else if (qNum == 2) {
         int y, x;
         scanf("%d %d", &y, &x);
         y--;
         x--;
         printf("%d\n", ground[y][x]);
      }

      else {
         printf("%d\n", cnt);
      }
   }
   return 0;
}