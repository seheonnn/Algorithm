#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> arr, dp;

int main() {
    cin >> n;
    arr.assign(n, 0);
    dp.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        dp[i] = arr[i]; // dp 초기값은 자기 자신
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) {
                dp[i] = max(dp[i], dp[j] + arr[i]);
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