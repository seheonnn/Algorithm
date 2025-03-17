#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int tc;
int k;
vector<int> arr;
vector<int> prefix;
vector<vector<int>> dp; // dp[i][j] : i번 파일부터 j번 파일까지 하나로 합치는 최소 비용
int main() {
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cin >> k;
        arr.assign(k + 1, 0);
        prefix.assign(k + 1, 0);
        dp.assign(k + 1, vector<int>(k + 1));

        for (int i = 1; i <= k; i++) {
            cin >> arr[i];
            prefix[i] = prefix[i - 1] + arr[i];
        }

        for (int len= 2; len <= k; len++) { // 현재 계산에 포함하는 파일 개수
            for (int i = 1; i + len - 1 <= k; i++) {
                int j = i + len - 1; // 현재 구간의 끝점 (i에서len - 1만큼 증가)
                dp[i][j] = INT_MAX;
                for (int r = i; r < j; r++) {
                    // i ~ j 구간 기준점 r
                    // 기존 dp[i][j] 값과 X1 + X2 + 현재 합치는 비용을 비교
                    dp[i][j] = min(dp[i][j], dp[i][r] + dp[r + 1][j] + (prefix[j] - prefix[i - 1]));
                }
            }
        }

        cout << dp[1][k] << endl;

    }
    return 0;
}