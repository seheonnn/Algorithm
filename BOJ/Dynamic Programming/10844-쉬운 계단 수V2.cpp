#include <iostream>
#include <cstring>

#define MOD 1000000000

using namespace std;

int n;

int main() {
    cin >> n;
    int dp[n + 1][10]; // dp[i][j] 길이가 i일 때 j로 끝나는 경우
    memset(dp, 0, sizeof(dp));

    for (int j = 0; j <= 9; j++) {
        dp[1][j] = 1;
    }

    dp[1][0] = 0;

    for (int i = 2; i <= n; i++) {
        for (int j = 0; j <= 9; j++) {
            if (j > 0) {
                dp[i][j] += dp[i - 1][j - 1]; // 0은 j + 1만
                dp[i][j] %= MOD;
            }
            if (j < 9) {
                dp[i][j] += dp[i - 1][j + 1]; // 9는 j - 1만
                dp[i][j] %= MOD;
            }
        }
    }

    int r = 0;
    for (int j = 0; j <= 9; j++) {
        r += dp[n][j];
        r %= MOD;
    }
    cout << r << endl;

    return 0;
}