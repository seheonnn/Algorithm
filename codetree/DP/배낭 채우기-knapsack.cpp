#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int n, m;
vector<int> weights;
vector<int> values;
vector<int> dp;
int main() {
    cin >> n >> m;

    weights.assign(n, 0);
    values.assign(n, 0);
    dp.assign(m + 1, 0);

    for (int i = 0; i < n; i++) {
        cin >> weights[i] >> values[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = m; j >= weights[i]; j--) {  // 중복 허용 X (역순)
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i]);
        }
    }

    int r = INT_MIN;
    for (int i = 0; i <= m; i++) {
        r = max(r, dp[i]);
    }

    cout << r << endl;

    return 0;
}
