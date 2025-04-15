// 백준 17404 RGB 2 DP

#include <iostream>
#include <vector>
#include <algorithm>
#define INF 1e9 // climits 사용시 overflow 발생

using namespace std;

int n;
vector<vector<int>> arr;

int main() {
    cin >> n;
    arr.assign(n, vector<int>(3));

    for (int i = 0; i < n; i++) {
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
    }

    int r = INF;
    for (int rgb = 0; rgb < 3; rgb++) {
        vector<vector<int>> dp(n, vector<int>(3, INF));

        dp[0][rgb] = arr[0][rgb];

        for (int i = 1; i < n; i++) {
            dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2]);
            dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1]);
        }

        for (int i = 0; i < 3; i++) {
            if (i != rgb) {
                r = min(r, dp[n - 1][i]);
            }
        }
    }

    cout << r << endl;
    return 0;
}
