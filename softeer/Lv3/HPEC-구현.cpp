// 소프티어 Lv3 HPEC 구현
#include <iostream>
#include <cmath>
#define MAX 200001
using namespace std;

int main() {

   int p[MAX];
   int c[MAX];

   int n;
   int x = 0;

   cin >> n;

   for (int i = 0; i < n;i++) {
      cin >> p[i] >> c[i];
   }

   for (int i = 0; i < n; i++) {
      if (abs(p[i] - x) <= c[i]) {
         x++;
      }
   }

   cout << x << "\n";
   return 0;
}