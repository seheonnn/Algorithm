// 백준 11053 가장 긴 증가하는 부분 수열 DP
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> arr, dp;

int main() {
    cin >> n;
    arr.assign(n, 0);
    dp.assign(n, 1); // 자기 자신 포함이므로 1부터 시작

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int r = 0;
    for (int i = 0; i < n; i++) {
        r = max(r, dp[i]);
    }

    cout << r << endl;
    return 0;
}