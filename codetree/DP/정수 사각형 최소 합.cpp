// 코드트리 정수 사각형 최소 합 DP
#include <iostream>

using namespace std;

int n;
int grid[100][100];
int dp[100][100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // 1, n
    // 시작점을 기준으로 행과 열을 초기화 !
    dp[0][n - 1] = grid[0][n - 1];
    for (int j = n - 2; j >= 0; j--) {
        dp[0][j] = dp[0][j + 1] + grid[0][j];
    }
    for (int i = 1; i < n; i++) {
        dp[i][n - 1] = dp[i - 1][n - 1] + grid[i][n - 1];
    }

    // 점화식 : dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j+1] + grid[i][j])
    for (int i = 1; i < n; i++) {
        for (int j = n - 2; j >= 0; j--) {
            // dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j + 1] + grid[i][j]);
            dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + grid[i][j];
        }
    }

    cout << dp[n - 1][0]; // n, 1

    return 0;
}
