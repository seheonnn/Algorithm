// 코드트리 동전 더하기 그리디
#include <iostream>
#include <vector>

using namespace std;

int ans = 0;
int n, k;
vector<int> coins;

int main() {
    cin >> n >> k;
    coins.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    for (int i = n - 1; i >= 0; i--) {
        if (k == 0) break;

        ans += (k / coins[i]);
        k %= coins[i];
    }

    cout << ans;

    return 0;
}

