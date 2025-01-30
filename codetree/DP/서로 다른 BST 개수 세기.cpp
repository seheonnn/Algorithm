// 코드 트리 서로 다른 BST 개수 세기 DP
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> dp;

int main() {
    cin >> n;

    dp.resize(n + 1, 0);

    dp[0] = 1;
    dp[1] = 1;

    // dp[n] = E(0 ~ n - 1) (dp[i] * dp[n - i - 1)
    for (int i = 2; i <= n; i++) {
        dp[i] = 0;
        for (int j = 0; j < i; j++) {
            dp[i] += dp[j] * dp[i - j - 1];
        }
    }

    cout << dp[n] << endl;

    return 0;
}
