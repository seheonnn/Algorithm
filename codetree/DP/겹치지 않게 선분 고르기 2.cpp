// 코드트리 겹치지 않게 선분 고르기 2 DP
#include <iostream>
#include <algorithm>
#define MAX 1001

using namespace std;

int n;
int dp[MAX];
pair<int, int> arr[MAX];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        arr[i] = {a, b};
        dp[i] = 1;
    }

    sort(arr, arr + n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j].second < arr[i].first) {
                dp[i] = max(dp[i],dp[j] + 1);
            }
        }
    }

    int r = 0;
    for (int i = 0; i < n; i++) {
        r = max(r, dp[i]);
    }

    cout << r;

}