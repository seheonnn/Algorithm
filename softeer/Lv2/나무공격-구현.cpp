// 소프티어 lv2 나무 공격 구현
#include <iostream>
#define MAX 100
using namespace std;
int main() {
   int n, m;
   int graph[MAX][MAX];
   cin >> n >> m;
   for (int i = 1; i <= n;i++) {
      for (int j = 1; j <= m;j++) {
         cin >> graph[i][j];
      }
   }

   int l1, r1;
   int l2, r2;
   cin >> l1 >> r1;
   cin >> l2 >> r2;

   for (int i = l1; i <= r1; i++) {
      for (int j = 1; j <= m; j++) {
         if (graph[i][j] == 1) {
            graph[i][j] = 0;
            break; // 한 행에서 처음 만나는 부분만 제거
         }
      }
   }

   for (int i = l2; i <= r2; i++) {
      for (int j = 1; j <= m; j++) {
         if (graph[i][j] == 1) {
            graph[i][j] = 0;
            break;
         }
      }
   }

   int cnt = 0;
   for (int i = 1; i <= n;i++) {
      for (int j = 1; j <= m;j++) {
         if (graph[i][j] == 1)
            cnt++;
      }
   }
   cout << cnt << "\n";

   return 0;
}