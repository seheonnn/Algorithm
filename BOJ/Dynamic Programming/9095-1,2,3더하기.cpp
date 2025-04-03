// 백준 9095 1, 2, 3 더하기 DP
#include <iostream>
#include <vector>

using namespace std;

int tc, n;
vector<int> dp;

int main() {
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cin >> n;
        dp.assign(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }

        cout << dp[n] << endl;
    }
    return 0;
}