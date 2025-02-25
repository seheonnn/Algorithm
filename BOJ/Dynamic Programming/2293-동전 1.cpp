#include <iostream>
#include <vector>

using namespace std;

int n, k;
vector<int> coins;
vector<int> dp; // dp[i] : i원을 만드는 경우의 수

int main() {
    cin >> n >> k;
    coins.assign(n + 1, 0);
    dp.assign(k + 1, 0);
    for (int i = 1; i <= n; i++){
        cin >> coins[i];
    }

    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = coins[i]; j <= k; j++) {
            dp[j] += dp[j - coins[i]];
        }
    }

    cout << dp[k] << endl;
    return 0;
}