// 백준 7579 앱 DP k-napsack
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> mem, cost,dp;
int main() {
    cin >> n >> m;
    mem.assign(n, 0);
    cost.assign(n, 0);

    for (int i = 0; i < n; i++) {
        cin >> mem[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> cost[i];
    }

    int maxCost = 100 * n; // 비활성화 최대 Cost
    dp.assign(maxCost + 1, 0); // dp[j] 비용이 j일 때 확보할 수 있는 최대 메모리 공간
    for (int i = 0; i < n; i++) {
        for (int j = maxCost; j >= cost[i]; j--) { // k-napsack은 무게 제한, 해당 문제에선 최소 cost를 계산하므로 maxCost에서 시
            dp[j] = max(dp[j], dp[j - cost[i]] + mem[i]);
        }
    }

    for (int i = 0; i <= maxCost; i++) {
        if (dp[i] >= m) {
            cout << i << endl;
            break;
        }
    }

    return 0;
}