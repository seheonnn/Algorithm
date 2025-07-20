// 코드트리 정수 사각형 최솟값의 최대 DP
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

    dp[0][0] = grid[0][0];

    // n, n까지의 경로들의 최솟값이 최대가 되도록
    for (int i = 1; i < n; i++) {
        dp[i][0] = min(dp[i - 1][0], grid[i][0]);
    }

    for (int j = 1; j < n; j++) {
        dp[0][j] = min(dp[0][j - 1], grid[0][j]);
    }

    // 위쪽 칸(dp[i-1][j])와 왼쪽 칸(dp[i][j-1]) 중 더 큰 값을 선택
    // 현재 칸의 값(grid[i][j])과 비교하여 최소값을 DP에 저장
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            // 이전 값들 끼리 비교는 최대
            // 현재 값과의 비교는 최소
            dp[i][j] = min(max(dp[i - 1][j], dp[i][j - 1]), grid[i][j]);
        }
    }

    cout << dp[n - 1][n - 1] << endl;

    return 0;
}
