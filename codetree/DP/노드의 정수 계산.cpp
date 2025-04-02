#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int>> graph;
vector<int> visited;
vector<int> arr;
vector<int> dp;

void DFS(int cur) {
    for (int next : graph[cur]) {
        if (visited[next] == -1) {
            visited[next] = 1;
            DFS(next);
        }
    }

    dp[cur] = arr[cur];
    for (int next : graph[cur]) {
        if (dp[next] > 0) {
            dp[cur] += dp[next];
        }
    }
}

int main() {
    cin >> n;
    graph.resize(n + 1);
    arr.resize(n + 1);
    visited.resize(n + 1, -1);
    dp.resize(n + 1);

    for (int i = 2; i <= n; i++) {
        int t, a, p;
        cin >> t >> a >> p;
        graph[p].push_back(i);
        arr[i] = (t == 1) ? a : -a;
    }

    DFS(1);
    cout << dp[1];

    return 0;
}