// 프로그래머스 2xn 타일링 DP
// #include <string>
// #include <vector>

// using namespace std;

// vector<int> dp;

// int solution(int n) {
//     dp.assign(n + 1, 0);
//     dp[0] = 1;
//     dp[1] = 1;

//     for (int i = 2; i <= n; i++) {
//         dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007;
//     }

//     return dp[n];
// }

// 누적합
using namespace std;

int solution(int n) {
    int mod = 1000000007;
    int prev1 = 1;
    int prev2 = 1;
    for (int i = 2; i <= n; i++) {
        int cur = (prev1 + prev2) % mod;
        prev2 = prev1;
        prev1 = cur;
    }

    return prev1;
}

