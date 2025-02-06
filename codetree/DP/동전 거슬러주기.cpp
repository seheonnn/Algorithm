// 코드 트리 동전 거슬러주기 DP
#include <iostream>
#include <climits>
#define MAX 10001

using namespace std;

int n, m;
int coin[MAX];
int dp[MAX]; // dp[i] : 금액 i를 이루기 위해 필요한 최소 동전 개수

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> coin[i];
    }

    dp[0] = 0;
    for (int i = 1; i <= m; i++) {
        dp[i] = INT_MAX;
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 0; j < n; j++) {
            if (i >= coin[j] and dp[i - coin[j]] != INT_MAX) {
                dp[i] = min(dp[i], dp[i - coin[j]] + 1);
            }
        }
    }

    if (dp[m] == INT_MAX) {
        cout << -1 << endl;
    } else {
        cout << dp[m] << endl;
    }

    return 0;
}
