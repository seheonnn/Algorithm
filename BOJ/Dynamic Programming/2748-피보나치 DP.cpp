// 백준 2748 피보나치 dp
#include <iostream>
#define MAX 91
using namespace std;
int main() {
   long long dp[MAX]; // 타입 주의 !
   int num;
   cin >> num;
   dp[0] = 0;
   dp[1] = 1;
   for (int i = 2;i <= num; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
   }

   cout << dp[num];
}