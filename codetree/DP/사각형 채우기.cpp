////코드트리 사각형 채우기 DP 다시
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> dp;

int main() {
    cin >> n;

    dp.resize(n + 1, 0);

    // dp[i] = 2 x i 크기의 사각형을 의미
    // 2 x n 크기의 사각형을 1 x 2 or 2 x 1 타일로 채우기
    dp[0] = 1; // 2 x 0 사각형에는 아무것도 놓지 않는 경우 하나
    dp[1] = 1; // 2 x 1 사각형에는 2 x 1 놓는 경우 하나

    // dp[i] = dp[i - 1] + dp[i - 2]
    for (int i = 2; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
    }

    cout << dp[n] << endl;

    return 0;
}