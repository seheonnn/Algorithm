// 백준 2579 계단 오르기 DP
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> dp;
vector<int> stairs;
int main() {
    cin >> n;
    dp.assign(n + 1, 0);
    stairs.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> stairs[i];
    }

    dp[0] = stairs[0];
    dp[1] = stairs[0] + stairs[1];
    for (int i = 2; i <= n; i++) {
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i]);
    }

    cout << dp[n] << endl;

    return 0;
}