// 코드트리 2차원 최대 증가 수열 DP
#include <iostream>
#include <climits>

using namespace std;

int n, m;
int grid[50][50];
int dp[50][50];

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
            dp[i][j] = -INT_MAX;
        }
    }

    dp[0][0] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // 현재 위치 : i, j
            for (int k = 0; k < i; k++) {
                for (int l = 0; l < j; l++) {
                    // 이전 위치 : k, l
                    // dp[k][k] == -INT_MAX라면 점프했기 때문에 방문하지 않은 곳임
                    if (dp[k][l] == -INT_MAX) {
                        continue;
                    }

                    // 이전 위치 값이 현재 위치 값보다 작을 때, dp 값을 갱신
                    if (grid[k][l] < grid[i][j]) {
                        dp[i][j] = max(dp[i][j], dp[k][l] + 1);
                    }
                }
            }
        }
    }

    int r = 0;
    // 도착 위치 상관 없
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            r = max(r, dp[i][j]);
        }
    }

    cout << r << endl;

    return 0;
}
