// 백준 2096 내려가기 DP
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int preMax[3], preMin[3];
int curMax[3], curMin[3];
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        if (i == 0) {
            preMax[0] = preMin[0] = a;
            preMax[1] = preMin[1] = b;
            preMax[2] = preMin[2] = c;
        } else {
            curMax[0] = max(preMax[0], preMax[1]) + a;
            curMax[1] = max({preMax[0], preMax[1], preMax[2]}) + b;
            curMax[2] = max(preMax[1], preMax[2]) + c;

            curMin[0] = min(preMin[0], preMin[1]) + a;
            curMin[1] = min({preMin[0], preMin[1], preMin[2]}) + b;
            curMin[2] = min(preMin[1], preMin[2]) + c;

            for(int i = 0; i < 3; i++) {
                preMax[i] = curMax[i];
                preMin[i] = curMin[i];
            }
        }
    }

    cout << max({preMax[0], preMax[1], preMax[2]}) << " " << min({preMin[0], preMin[1], preMin[2]}) << "\n";

    return 0;
}