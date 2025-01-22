#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> arr;
vector<int> dp;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    arr.resize(n, 0);
    dp.resize(n, 0);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    dp[0] = arr[0];

    for (int i = 1; i < n; i++) {
        // 이전까지의 원소를 더한값 + 현재 원소 vs 현재 원소부터 새로 시작
        // 이를 비교하여 큰 값을 dp 저장
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
    }

    int r = -1000;
       for (int i = 0; i < n; i++) {
        r = max(r, dp[i]);
    }

    cout << r;

    return 0;
}