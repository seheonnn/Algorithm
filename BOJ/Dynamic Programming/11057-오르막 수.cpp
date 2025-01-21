// 백준 11057 오르막 수 DP
#include <iostream>
#define MOD 10007

using namespace std;

int n;
int dp[1001][10]; // dp[i][j] : i의 길이를 가지며 j로 끝나는 수의 개수

int main() {
    scanf("%d", &n);

    for (int j = 0; j <= 9; j++) {
        dp[1][j] = 1; // 길이 1에서 1~9로 끝나는 경우의 수는 각각 1개
    }

    // 길이 1에서는 숫자 하나만 있으면 되므로,
    // 모든 숫자(0~9)가 한 자리수 오르막 수가 됨
    // dp[1][0] = 1이 맞음 -> 계단수와 차이

    for (int i = 2; i<= n; i++) {
        for (int j = 0; j <= 9; j++) {
            if (j == 0) {
                dp[i][0] = 1; // 길이가 i이고 마지막 숫자가 j인 오르막 수는 항상 1
                continue;
            }
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            dp[i][j] %= MOD;
        }
    }

    int r = 0;
    for (int j = 0; j <= 9; j++) {
        r += dp[n][j];
        r %= MOD;
    }

    printf("%d\n", r);

    return 0;
}