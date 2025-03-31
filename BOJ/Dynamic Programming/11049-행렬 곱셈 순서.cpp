// 백준 11049 행렬 곱셈 순서 DP
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int n;
vector<pair<int, int>> arr;
vector<vector<int>> dp; // i번째 행렬부터 j번째 행렬까지 곱하는 데 필요한 곱셈 연산 횟수

int main() {
    cin >> n;
    dp.assign(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        arr.push_back({tmp1, tmp2});
    }

    for (int len = 1; len < n; len++) {
        for (int i = 0; i + len < n; i++) {
            int j = i + len;
            dp[i][j] = INT_MAX;

            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k + 1][j] + arr[i].first * arr[k].second * arr[j].second;
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }

    cout << dp[0][n - 1];

    return 0;
}