#include <string>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

vector<vector<pair<int, int>>> graph;
vector<int> dist;

void Dijkstra(int start, int n) {
    dist.assign(n + 1, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push({dist[start], start});

    while(!pq.empty()) {
        int d = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if (dist[cur] < d) continue;
        for (auto& tmp : graph[cur]) {
            int next = tmp.first;
            int w = tmp.second;
            int new_dist = d + w;
            if (dist[next] > new_dist) {
                dist[next] = new_dist;
                pq.push({dist[next], next});
            }
        }
    }
}
int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 0;
    graph.assign(n + 1, vector<pair<int, int>>());

    for (auto& tmp : fares) {
        graph[tmp[0]].push_back({tmp[1], tmp[2]});
        graph[tmp[1]].push_back({tmp[0], tmp[2]});
    }

    Dijkstra(s, n);
    vector<int> fromS = dist;
    Dijkstra(a, n);
    vector<int> fromA = dist;
    Dijkstra(b, n);
    vector<int> fromB = dist;

    int r = INT_MAX;
    for (int i = 1; i <= n; i++) { // 헤어지는 지점 모두 고려
        if (fromS[i] != INT_MAX && fromA[i] != INT_MAX && fromB[i] != INT_MAX) {
            r = min(r, fromS[i] + fromA[i] + fromB[i]);
        }
    }

    return r;
}