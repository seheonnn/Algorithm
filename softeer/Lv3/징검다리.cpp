// 소프티어 징검다리
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 3 * 10 * 10 * 10
using namespace std;

int main() {
   int n;
   cin >> n;

   vector<int> arr(n);
   vector<int> dp(n, 1); // DP 배열 초기화

   for (int i = 0; i < n; i++) {
      cin >> arr[i];
   }

   for (int i = 1; i < n; i++) {
      for (int j = 0; j < i; j++) {
         if (arr[i] > arr[j]) {
            dp[i] = max(dp[i], dp[j] + 1);
         }
      }
   }

   int r = 0;
   for (int i = 0;i < n;i++) {
      r = max(r, dp[i]);
   }
   cout << r << "\n";

   return 0;
}