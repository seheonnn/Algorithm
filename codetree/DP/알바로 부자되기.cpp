// 코드트리 알바로 부자 되기 DP
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int n;
vector<int> s;
vector<int> e;
vector<int> p;
vector<int> dp; // dp[i] 마지막으로 i번쨰 알바를 골랐을 떄 얻을 수 있는 최대 수익

int main() {
    cin >> n;

    s.assign(n + 1, 0);
    e.assign(n + 1, 0);
    p.assign(n + 1, 0);
    dp.assign(n + 1, 0);
    for (int i = 0; i <= n; i++) {
        dp[i] = INT_MIN;
    }

    s[0] = e[0] = p[0] = 0;
    dp[0] = 0; // 아무런 알바를 진행하지 못함

    for (int i = 1; i <= n; i++) {
        cin >> s[i] >> e[i] >> p[i];
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) { // i 번쨰 알바와 i 번쨰 앞의 알바들과 비교
            if (e[j] < s[i]) { // 알바끼리 겹치지 않아야
                dp[i] = max(dp[i], dp[j] + p[i]); // dp[i] 갱신
            }
        }
    }

    int r = 0;
    for (int i = 0; i <= n; i++) {
        r = max(r, dp[i]);
    }

    cout << r << endl;
}