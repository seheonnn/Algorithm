// 백준 1504 특정한 최단 경로 다익스트라
#include <iostream>
#include <vector>
#include <climits>
#include <deque>
#define MAX 801

using namespace std;

int n, e;
int v1, v2;
vector<vector<pair<int, int>>> graph;
int dist[MAX];

void Dijkstra(vector<vector<pair<int, int>>>& graph, int v, int dist[]) {
    for (int i = 1; i <= n; i++) {
        dist[i] = INT_MAX;
    }

    deque<pair<int, int>> queue;
    dist[v] = 0;
    queue.push_back({v, 0});

    while (!queue.empty()) {
        int cur = queue.front().first;
        int dst = queue.front().second;
        queue.pop_front();

        if (dst > dist[cur]) continue;
        for (auto edge : graph[cur]) {
            int next = edge.first;
            int w = edge.second;
            int new_dist = dst + w;

            if (new_dist < dist[next]) {
                dist[next] = new_dist;
                queue.push_back({next, new_dist});
            }
        }
    }
}

int main() {
    scanf("%d %d", &n, &e);
    graph.resize(n + 1);

    for (int i = 0; i < e; i++)  {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }
    scanf("%d %d", &v1, &v2);

    Dijkstra(graph, 1, dist);
    int startToV1 = dist[v1];
    int startToV2 = dist[v2];

    Dijkstra(graph, v1, dist);
    int v1ToV2 = dist[v2];
    int v1ToN = dist[n];

    Dijkstra(graph, v2, dist);
    int v2ToV1 = dist[v1];
    int v2ToN = dist[n];

    // 1 -> v1 -> v2 -> n
    int path1 = startToV1 + v1ToV2 + v2ToN;
    // 1 -> v2 -> v1 -> n
    int path2 = startToV2 + v2ToV1 + v1ToN;

    // INT_MAX + 5 한다고 INT_MAX 유지되지 않음. 정수 오버플로 문제.
    // path1 >= INT_MAX 같은 조건은 부정확함

    if (startToV1 == INT_MAX || v1ToV2 == INT_MAX || v2ToN == INT_MAX ||
    startToV2 == INT_MAX || v2ToV1 == INT_MAX || v1ToN == INT_MAX)
        printf("-1\n");
    else
        printf("%d\n", path1 < path2 ? path1 : path2);

    return 0;
}