#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> t;
vector<int> p;
vector<int> dp;

int main() {
    cin >> n;
    t.assign(n + 1, 0);
    p.assign(n + 1, 0);
    dp.assign(n + 2, 0);

    for (int i = 1; i <= n;i ++) {
        cin >> t[i] >> p[i];
    }

    for (int i = 1; i <= n; i++) {
        dp[i] = max(dp[i], dp[i - 1]);

        int nextDay = i + t[i];
        if (nextDay <= n + 1) {
            dp[nextDay] = max(dp[nextDay], dp[i] + p[i]);
        }
    }

    cout << max(dp[n], dp[n + 1]);
    return 0;
}