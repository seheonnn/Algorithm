// 코드트리 최대 증가 부분 수열 DP
#include <iostream>

using namespace std;

int n;
int grid[1000];
int dp[1000];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
        // dp[i]는 i까지 증가하는 수열의 길이. 최초 자기자신인 1로 시작
        dp[i] = 1;
    }

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (grid[j] < grid[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int r = 0;
    for (int i = 0; i < n; i++) {
        r = max(r, dp[i]);
    }

    cout << r << endl;

    return 0;
}
