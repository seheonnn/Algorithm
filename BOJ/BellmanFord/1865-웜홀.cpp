#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int n, m, w, tc;
vector<vector<pair<int, int>>> graph;
vector<int> dist;

bool BellmanFord(int start) {
    dist[start] = 0;

    for (int i = 1; i < n; i++) {
        for (int cur = 1; cur <= n; cur++) {
            for (auto edges : graph[cur]) {
                int next = edges.first;
                int weight = edges.second;
                if (dist[cur] != INT_MAX && dist[next] > dist[cur] + weight) {
                    dist[next] = dist[cur] + weight;
                }
            }
        }
    }

    // 음수 사이클 검사
    for (int cur = 1; cur <= n; cur++) {
        for (auto edges : graph[cur]) {
            int next = edges.first;
            int weight = edges.second;
            if (dist[cur] != INT_MAX && dist[next] > dist[cur] + weight) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cin >> n >> m >> w;

        // graph.resize(n + 1);
        // dist.resize(n + 1, INT_MAX);

        graph.assign(n + 1, vector<pair<int, int>>());
        dist.assign(n + 1, INT_MAX);

        for (int i = 0; i < m; i++) {
            int s, e, t;
            cin >> s >> e >> t;
            graph[s].push_back({e, t});
            graph[e].push_back({s, t});
        }

        for (int i = 0; i < w; i++) {
            int s, e, t;
            cin >> s >> e >> t;
            graph[s].push_back({e, -t});
        }

        bool r = false;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == INT_MAX) {  // 아직 방문하지 않은 노드
                if (BellmanFord(i)) {
                    r = true;
                    break;
                }
            }
        }

        cout << (r ? "YES" : "NO") << '\n';
    }
    return 0;
}
