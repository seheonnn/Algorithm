#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int n, k;
vector<int> weights;
vector<int> values;
vector<vector<int>> dp;

int main() {
    cin >> n >> k;
    weights.assign(n + 1, 0);
    values.assign(n + 1, 0);
    dp.assign(n + 1, vector<int>(k + 1)); // dp[n][k] 크기

    for (int i = 1; i <= n; i++) {
        cin >> weights[i] >> values[i];
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            if (j >= weights[i]) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i]);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    int r = INT_MIN;
    for (int j = 0; j <= k; j++) {
        r = max(r, dp[n][k]);
    }

    cout << r << endl;

    return 0;
}