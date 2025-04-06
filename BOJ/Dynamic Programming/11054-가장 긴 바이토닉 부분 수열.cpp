// 백준 11054 가장 긴 바이토닉 부분 수열 LIS&LDS
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> arr, dp1, dp2;

int main() {
    cin >> n;
    arr.assign(n, 0);
    dp1.assign(n, 1);
    dp2.assign(n, 1);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // LIS
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j]) {
                dp1[i] = max(dp1[i], dp1[j] + 1);
            }
        }
    }

    // LDS 바이토닉 수열에선 감소하는 방향으로 구해야
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                dp2[i] = max(dp2[i], dp2[j] + 1);
            }
        }
    }

    int r = 0;
    for (int i = 0; i < n; i++) {
        r = max(r, dp1[i] + dp2[i] - 1);
    }

    cout << r << endl;

    return 0;
}