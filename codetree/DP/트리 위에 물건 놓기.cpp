#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> graph;
vector<int> visited;
vector<vector<int>> dp;
void DFS(int cur) {
    for (int next : graph[cur]) {
        if (visited[next] == -1) {
            visited[next] = cur;
            DFS(next);
        }
    }

    dp[cur][0] = 0; // cur 노드에 아무 물건도 놓지 않는 경우
    dp[cur][1] = 1; // cur 노드에 물건을 놓는 경우, 시작은 1
    for (int next : graph[cur]) {
        if (visited[next] != cur) continue;

        // 경우 1) cur 노드에 물건을 놓지 않는 경우 cur 노드의 자식들인 next 노드는 j가 1인 경우만 선택 가능
        dp[cur][0] += dp[next][1];

        // 경우 2) cur 노드에 물건을 놓는 경우 cur 노들의 자식들인 next 노드에 대해서는 j가 0, 1인 두 경우 모두 선택 가능하므로 모두 더함
        dp[cur][1] += min(dp[next][0], dp[next][1]);
    }
}

int main() {

    cin >> n;
    graph.resize(n + 1); // graph.resize(n + 1, vector<int>(n + 1)); 필요한 간선만 초기화 해야
    visited.resize(n + 1, -1);
    dp.resize(n + 1, vector<int>(2));

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    visited[1] = 1;
    DFS(1);

    cout << min(dp[1][0], dp[1][1]);

    return 0;
}