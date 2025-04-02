#include <iostream>
#include <vector>
#include <climits>
#include <queue>
#include <algorithm>  // reverse() 함수를 위해 추가

using namespace std;

vector<vector<pair<int, int>>> graph;
vector<int> dist;
vector<int> prevCity;  // prev는 STL 함수와 혼동될 수 있으니 이름 변경 (예: prevCity)
vector<int> path;
int n, m;

void Dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[start] = 0;
    pq.push({dist[start], start});

    while (!pq.empty()) {
        int d = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if (d > dist[cur]) continue;

        for (auto edge : graph[cur]) {
            int next = edge.first;
            int w = edge.second;
            int new_dist = d + w;
            if (new_dist < dist[next]) {
                dist[next] = new_dist;
                prevCity[next] = cur;
                pq.push({dist[next], next});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    graph.resize(n + 1);
    dist.resize(n + 1, INT_MAX);
    prevCity.resize(n + 1, -1);

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
    }

    int s, e;
    cin >> s >> e;

    Dijkstra(s);
    cout << dist[e] << endl;

    int cur = e;
    while (cur != -1) {
        path.push_back(cur);
        cur = prevCity[cur];
    }
    reverse(path.begin(), path.end());

    cout << path.size() << endl;
    for (int city : path) {
        cout << city << " ";
    }

    return 0;
}
