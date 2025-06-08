#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int n, k;
map<int, int> arr;

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        arr[tmp]++;
    }

    vector<pair<int, int>> v(arr.begin(), arr.end());

    sort(v.begin(), v.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first > b.first;
    });

    for (int i = 0; i < k; i++) {
        cout << v[i].first << ' ';
    }

    return 0;
}
