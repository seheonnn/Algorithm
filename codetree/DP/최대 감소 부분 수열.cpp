// 코드트리 최대 감소 부분 수열 DP
#include <iostream>

using namespace std;

const int MAX = 1000;

int n;
int grid[MAX];
int dp[1000];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
        dp[i] = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (grid[i] < grid[j]) {
                // min 아님. 길이 최대
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
