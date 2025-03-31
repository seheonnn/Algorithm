// 백준 1806 부분합 투포인터
#include <iostream>
#include <vector>

using namespace std;

int n, s;
vector<int> arr;
int main() {
    cin >> n >> s;
    arr.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int r = n + 1;
    int sum = 0;
    int start = 0;

    for (int end = 0; end < n; end++) {
        sum += arr[end];
        while (sum >= s) {
            r = min(r, end - start + 1);
            sum -= arr[start];
            start++;
        }
    }

    if (r == n + 1) cout << 0 << "\n";
    else cout << r << "\n";

    return 0;
}