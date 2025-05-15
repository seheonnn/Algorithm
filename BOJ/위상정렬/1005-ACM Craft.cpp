#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int tc, n, k, w;
vector<int> dist, visited, dp;
vector<vector<int>> graph;
void BFS() {
    // priority_queue<int, vector<int>, greater<int>> q;
    queue<int> q; // 처리 순서 조건이 있으면 우선순위 큐, 아니라면 일반 큐로도 가능
    for (int i = 1; i <= n; i++) {
        if (visited[i] == 0) {
            q.push(i);
            dp[i] = dist[i];
        }
    }

    while(!q.empty()) {
        int cur = q.front();
        // int cur = q.top();
        q.pop();

        for (auto next : graph[cur]) {
            dp[next] = max(dp[next], dp[cur] + dist[next]);
            visited[next]--; // 진입 차수 감소

            if(visited[next] == 0) {
                q.push(next);
            }
        }
    }
}

int main() {
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cin >> n >> k;
        dist.assign(n + 1, 0);
        visited.assign(n + 1, 0);
        dp.assign(n + 1, 0);
        graph.assign(n + 1, vector<int>());

        for (int i = 1; i <= n; i++) {
            cin >> dist[i];
        }

        for (int i = 0; i < k; i++) {
            int x, y;
            cin >> x >> y;
            graph[x].push_back(y);
            visited[y]++; // 진입 순서
        }

        cin >> w;
        BFS();
        cout << dp[w] << "\n";
    }



    return 0;
}