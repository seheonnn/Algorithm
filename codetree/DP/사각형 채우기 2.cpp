// 코드 트리 사각형 채우기2 DP
#include <iostream>
#include <vector>
#define MOD 10007
using namespace std;

int n;
vector<int> dp;

int main() {
    cin >> n;

    dp.resize(n + 1, 0);
    dp[0] = 1;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        // 점화식 : dp[i]  = dp[i - 1] + 2 * dp[i - 2]
        //         2 x 1,      1 x 2,     2 x 2
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 2]) % MOD;
    }

    cout << dp[n] << endl;

    return 0;
}