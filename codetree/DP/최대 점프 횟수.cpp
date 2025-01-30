// 코드트리 최대 점프 횟수 DP
#include <iostream>
#include <climits>
using namespace std;

int n;
int arr[1000];
int dp[1000];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        dp[i] = -INT_MAX;
    }

    dp[0] = 0;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] == -INT_MAX) { // 점프한 부분
                continue; // 건너뜀
            }

            // 현재 위치(i)로 점프 가능한지 확인
            if (j + arr[j] >= i) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int r = -INT_MAX;
    for (int i = 0; i < n; i++) {
        r = max(r, dp[i]);
    }

    cout << r << endl;

    return 0;
}
