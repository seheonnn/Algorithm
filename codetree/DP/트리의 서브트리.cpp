#include <iostream>
#include <vector>

using namespace std;

int n, r, q;
vector<vector<int>> graph;
vector<int> visited;
vector<int> dp;

void DFS(int cur) {
    dp[cur] = 1;  // 자기 자신을 포함해서 시작
    for (int next : graph[cur]) {
        if (visited[next] == -1) {
            visited[next] = 1;
            DFS(next);
            dp[cur] += dp[next];  // 서브트리 크기를 더함
        }
    }
}

int main() {
    cin >> n >> r >> q;
    graph.resize(n + 1);
    visited.resize(n + 1, -1);
    dp.resize(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    visited[r] = 1;
    DFS(r);

    for (int i = 0; i < q; i++) {
        int u;
        cin >> u;
        cout << dp[u] <<endl;
    }

    return 0;
}