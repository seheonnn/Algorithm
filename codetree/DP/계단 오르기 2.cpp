#include <iostream>
#include <vector>
#define MAX 1001

using namespace std;

int n;
int coin[MAX];
int dp[MAX][4];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> coin[i];
    }
    // 남우는 1계단을 오르는 행동을 최대 3번까지 하거나, 2개의 계단을 한 번에 오를 수 있음
    dp[1][1] = coin[1]; // 1계단에 위치한 경우는 1계단을 한 번 오른 경우뿐
    dp[2][0] = coin[2]; // 2계단에 위치한 경우는 한 번에 2계단을 오른 경우와
    dp[2][2] = coin[1] + coin[2]; // 1계단씩 2번 오른 경우가 있음

    // dp[i][j] : i번 위치에 도착했을 때 1계단을 j번 오름
    for (int i = 3; i <= n; i++) {
        for (int j = 0; j <= 3; j++) { // 1계단을 오른 횟수 j번, 최대 3번 오를 수 있으므로 3
            if (dp[i - 2][j] != 0) { // 한 번에 2계단을 오른 경우, j는 그대로
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i]);
            }
            if (j && dp[i - 1][j - 1] != 0) { // 1계단 오른 경우, 즉 1계단을 1번 올랐으므로 i, j 1씩 증가임
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin[i]);
            }
        }
    }

    int r = 0;
    for (int j = 0; j <= 3; j++) {
        r = max(r, dp[n][j]);
    }

    cout << r; // 결과 출력
    return 0;
}
