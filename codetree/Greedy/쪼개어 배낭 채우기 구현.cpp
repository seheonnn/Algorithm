#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

int n, m;
vector<tuple<double, int, int>> pack;
double ans = 0;
int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        int w, v;
        cin >> w >> v;
        pack.push_back({(double) v / w, w, v});
    }
    sort(pack.rbegin(), pack.rend());

    for (int i = 0; i < n; i++) {
        auto [tmp, w, v] = pack[i];

        if (m >= w) {
            m -= w;
            ans += v;
        } else {
            ans += (double) m / w * v; // 남은 무게만큼만 넣기
            break;
        }
    }

    printf("%.3lf", ans);

    return 0;
}
