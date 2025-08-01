#include <iostream>
#include <vector>
using namespace std;

int solution(int n) {
    const int MOD = 1000000007;

    if (n % 2 == 1) return 0; // 3 x n은 n이 홀수면 절대 채울 수 없음

    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    dp[2] = 3;

    for (int i = 4; i <= n; i += 2) {
        dp[i] = dp[i - 2] * 3 % MOD; // 마지막 3 x 2 칸을 채우는 3가지 경우의 수
        for (int j = i - 4; j >= 0; j -= 2) {
            dp[i] = (dp[i] + dp[j] * 2 % MOD) % MOD;
        }
    }

    return dp[n];
}
