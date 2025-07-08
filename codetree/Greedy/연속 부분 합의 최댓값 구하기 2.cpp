// 코드트리 연속 부분 합의 최댓값 구하기 2 그리디
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int cur = a[0];
    int ans = a[0];

    for (int i = 1; i < n; i++) {
        cur = max(a[i], cur + a[i]); // 새로 시작 or 계속 더함
        ans = max(ans, cur);
    }

    cout << ans << endl;
    return 0;
}

