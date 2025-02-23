// 백준 1504 특정한 최단 경로 다익스트라
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <queue>

using namespace std;

int n, e, v1, v2;
int startToV1, startToV2, v1ToV2, v2ToV1, v1ToN, v2ToN;
vector<vector<pair<int, int>>> graph;
vector<int> dist;

void Dijkstra(int v) {
    dist[v] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({dist[v], v});

    while(!pq.empty()) {
        int d = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if (d > dist[cur]) continue;
        for (auto edges : graph[cur]) {
            int next = edges.first;
            int w = edges.second;
            int new_dist = w + d;
            if (dist[next] > new_dist) {
                dist[next] = new_dist;
                pq.push({dist[next], next});
            }
        }
    }
}

int main() {
    cin >> n >> e;
    graph.assign(n + 1, vector<pair<int, int>>());
    dist.assign(n + 1, INT_MAX);

    for (int i = 0; i < e; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    cin >> v1 >> v2;

    Dijkstra(1);
    startToV1 = dist[v1];
    startToV2 = dist[v2];

    dist.assign(n + 1, INT_MAX);
    Dijkstra(v1);
    v1ToV2 = dist[v2];
    v1ToN = dist[n];

    dist.assign(n + 1, INT_MAX);
    Dijkstra(v2);
    v2ToV1 = dist[v1];
    v2ToN = dist[n];

    int r = INT_MAX;
    if (startToV1 == INT_MAX || startToV2 == INT_MAX || v1ToV2 == INT_MAX || v2ToV1 == INT_MAX || v1ToN == INT_MAX || v2ToN == INT_MAX) {
        r = -1;
    } else {
        r = min(startToV1 + v1ToV2 + v2ToN, startToV2 + v2ToV1 + v1ToN);
    }

    cout << r;
    return 0;
}