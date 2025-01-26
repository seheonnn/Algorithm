#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define MAX 100000
using namespace std;

int n, u, v, w;
vector<pair<int, int>> graph[MAX];
int visited[MAX];

// void dfs(int v, int dist) {
//     for (auto &edge : graph[v]) {
//         int cur = edge.first;
//         int w = edge.second;
//         if (visited[cur] == -1) {
//             visited[cur] = dist + w;
//             dfs(cur, visited[cur]);
//         }
//     }
// }

void bfs(int v, int dist) {
    queue<pair<int, int>> q;
    q.push({v, dist});
    while (!q.empty()) {
        v = q.front().first;
        dist = q.front().second;
        q.pop();
        for (auto &edge : graph[v]) {
            int cur = edge.first;
            int w = edge.second;
            if (visited[cur] == -1) {
                visited[cur] = dist + w;
                q.push({cur, visited[cur]});
            }
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n + 1; i++) {
        visited[i] = -1;
    }

    for (int i = 0; i < n - 1; i++) {
        cin >> u >> v >> w;
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, w);
    }

    visited[1] = 0;
    bfs(1, 0);

    int farthest_node = 1;
    for (int i = 1; i <= n; i++) {
        if (visited[i] > visited[farthest_node]) {
            farthest_node = i;
        }
    }

    for (int i = 0; i < n + 1; i++) {
        visited[i] = -1;
    }
    visited[farthest_node] = 0;
    bfs(farthest_node, 0);
    int result = *max_element(visited + 1, visited + n + 1);
    cout << result << '\n';

    return 0;
}