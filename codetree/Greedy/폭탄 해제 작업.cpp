// 코드트리 폭탄 해제 작업 그리디
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n;
vector<pair<int, int>> arr;
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int s, t;
        cin >> s >> t;
        arr.push_back({t, s});
    }

    sort(arr.begin(), arr.end());

    priority_queue<int, vector<int>, greater<int>> pq;

    for (auto [t, s] : arr) {
        pq.push(s);
        if (pq.size() > t) {
            pq.pop();
        }
    }

    int r = 0;
    while(!pq.empty()) {
        r += pq.top();
        pq.pop();
    }
    cout << r << endl;

    return 0;
}

