#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<pair<int, int>> arr;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        arr.push_back({y, x});
    }

    sort(arr.begin(), arr.end());

    int left = 0, right = arr.size() - 1;
    int r = 0;
    while (left <= right) {
        int minVal = arr[left].first;
        int minCnt = arr[left].second;

        int maxVal = arr[right].first;
        int maxCnt = arr[right].second;

        int pairCnt = (left == right) ? minCnt / 2 : min(minCnt, maxCnt);

        r = max(r, minVal + maxVal);

        arr[left].second -= pairCnt;
        arr[right].second -= pairCnt;

        // 포인터 이동
        if (arr[left].second == 0) left++;
        if (arr[right].second == 0) right--;
    }

    cout << r << endl;

    return 0;
}
