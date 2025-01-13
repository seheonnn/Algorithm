// 코드트리 계단 오르기 DP
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> dp;
int main() {
    cin >> n;

    dp.resize(n + 1, 0);

    dp[0] = 1;
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    for (int i = 4; i <= n; i++) {
        dp[i] = (dp[i - 2] + dp[i - 3]) % 10007;
    }

    cout << dp[n] << endl;

    return 0;
}