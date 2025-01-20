// 코드트리 피보나치 수 DP
#include <iostream>
#include <vector>

using namespace std;

int N;

int main() {
    cin >> N;

    vector<int> dp(N + 1);
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;
    for (int i = 3; i <= N; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[N];

    return 0;
}