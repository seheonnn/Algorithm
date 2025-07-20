#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {

    vector<vector<int>> graph (n + 1, vector<int> (n + 1, 0));

    for (auto tmp : results) {
        graph[tmp[0]][tmp[1]] = true;
    }

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (graph[i][k] && graph[k][j]) {
                    graph[i][j] = true;
                }
            }
        }
    }

    int r = 0;
    for (int i = 1; i <= n; i++) {
        int cnt = 0;
        for (int j = 1; j <= n; j++) {
            if (graph[i][j] || graph[j][i]) cnt++;
        }

        if (cnt == n - 1) r++;
    }

    return r;
}