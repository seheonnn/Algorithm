// 프로그래머스 보행자 천국 DP
#include <vector>

using namespace std;

int MOD = 20170805;

int solution(int m, int n, vector<vector<int>> city_map) {
    vector<vector<vector<int>>> dp(m , vector<vector<int>>(n, vector<int>(2)));
    dp[0][0][0] = 0;
    dp[0][0][1] = 1;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (city_map[i][j] == 1) continue;

            if (i + 1 < m && city_map[i + 1][j] != 1) { // 아래로 가는 경우
                if (city_map[i][j] == 2) { // 현재 위치가 2면 직진만
                    dp[i + 1][j][0] = (dp[i][j][0]) % MOD;
                } else {
                    dp[i + 1][j][0] = (dp[i][j][0] + dp[i][j][1]) % MOD;
                }
            }


            if (j + 1 < n && city_map[i][j + 1] != 1) { // 우측으로 가는 경우
                if (city_map[i][j] == 2) { // 현재 위치가 2면 직진만
                    dp[i][j + 1][1] = (dp[i][j][1]) % MOD;
                } else {
                    dp[i][j + 1][1] = (dp[i][j][1] + dp[i][j][0]) % MOD;
                }
            }
        }
    }
    return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD;
}