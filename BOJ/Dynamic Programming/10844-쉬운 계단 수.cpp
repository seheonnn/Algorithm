// 백준 10844 쉬운 계단 수 DP
#include <iostream>
#define MOD 1000000000

using namespace std;

int n;
int dp[101][10]; // dp[i][j] : i의 길이를 가지며 j로 끝나는 수의 개수

int main() {
    scanf("%d", &n);

    for (int j = 0; j <= 9; j++) {
        dp[1][j] = 1; // 길이 1에서 1~9로 끝나는 경우의 수는 각각 1개
    }

    dp[1][0] = 0; // 0으로 끝나고 한 자리수인 계단 수는 없음

    for (int i = 2; i <= n; i++) { // 길이 i
        for (int j = 0; j <= 9; j++) {  // 마지막 숫자 j로
            // 예를들어 5로 끝나는 계단 수를 구한다고 가정하면
            // 4로 끝나고 뒤에 5가 붙는 경우, 6으로 끝나고 뒤에 5가 붙는 경우 두 가지임
            if (j > 0) {
                dp[i][j] += dp[i - 1][j - 1];
                dp[i][j] %= MOD;
            }
            if (j < 9) {
                dp[i][j] += dp[i - 1][j + 1];
                dp[i][j] %= MOD;
            }
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