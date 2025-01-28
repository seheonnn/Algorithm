//코드트리 사각형 채우기3 DP
#include <iostream>
#include <vector>
#define MOD 1000000007
using namespace std;

int n;
vector<long long> dp; // MOD 값이 매우 크므로 long long 자료형 주의

int main() {
    cin >> n;

    dp.resize(n + 1, 0);
    dp[0] = 1;
    dp[1] = 2;

    // dp[i-1]*2 : 끝에 1 x 2 타일을 추가하는 경우 두 가지 1x2 두 개씩, 2 x 1 두 개씩
    for (int i = 2; i <= n; i++) {
        dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2]) % MOD;

        for (int j = i - 3; j >= 0; j--) { // 남은 부분 2 x j 타일로 채우기
            dp[i] = (dp[i] + 2 * dp[j]) % MOD;
        }
    }

    cout << dp[n] << endl;

    return 0;
}