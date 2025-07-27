#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> cards) {
    int n = cards.size();
    vector<int> visited(n , false);
    vector<int> cycleSize;

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            int cnt = 0;
            int cur = i;
            while(!visited[cur]) {
                visited[cur] = true;
                cur = cards[cur] - 1;
                cnt++;
            }
            cycleSize.push_back(cnt);
        }
    }

    sort(cycleSize.rbegin(), cycleSize.rend());
    if (cycleSize.size() < 2 ) return 0; // 사이클이 1개뿐이면 점수는 0
    return cycleSize[0] * cycleSize[1];
}