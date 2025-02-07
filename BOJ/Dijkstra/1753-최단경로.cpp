// 백준 1753 최단경로 다익스트라
#include <iostream>
#include <vector>
#include <climits>
// #include <deque>
#include <queue>
#define MAX 20001

using namespace std;

int v, e, k;
vector<vector<pair<int, int>>> graph;
int dist[MAX];

// void Dijkstra(vector<vector<pair<int, int>>> graph, int start, int dist[]) {
//     for (int i = 1; i <= v; i++)
//         dist[i] = INT_MAX;

//     dist[start] = 0;

//     deque<pair<int, int>> queue;
//     queue.push_back({dist[start], start});

//     while(!queue.empty()) {
//         int d = queue.front().first;
//         int cur = queue.front().second;
//         queue.pop_front();

//         if (d > dist[cur]) continue;

//         for (auto& edge : graph[cur]) {
//             int next = edge.first;
//             int w = edge.second;
//             int new_dist = d + w;

//             if (new_dist < dist[next]) {
//                 dist[next] = new_dist;
//                 queue.push_back({dist[next], next});
//             }
//         }
//     }
// }

// 다익스트라는 우선순위 큐를 사용하는 것이 더 빠르다 !!
void Dijkstra_priority(vector<vector<pair<int, int>>> graph, int start, int dist[]) {
    for (int i = 1; i <= v; i++)
        dist[i] = INT_MAX;

    dist[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    pq.push({dist[start], start}); // 가중치를 앞에 놓는 게 효율성이 더 좋음

    while(!pq.empty()) {
        int d = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if (d > dist[cur]) continue;

        for (auto& edge : graph[cur]) {
            int next = edge.first; // 이건 graph에서 가져오므로 우선순위 큐랑 헷갈리지 않기 !
            int w = edge.second;
            int new_dist = d + w;

            if (new_dist < dist[next]) {
                dist[next] = new_dist;
                pq.push({dist[next], next});
            }
        }
    }
}

int main() {
    scanf("%d %d", &v, &e);
    scanf("%d", &k);
    graph.resize(v + 1);
    for (int i = 0; i < e; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        graph[u].push_back({v, w});
        // graph[v].push_back({u, w}); // 양방향 아님 주의
    }

    // Dijkstra(graph, k, dist);
    Dijkstra_priority(graph, k, dist);

    for (int i = 1; i <= v; i++) {
        if (dist[i] == INT_MAX)
            printf("INF\n");
        else
            printf("%d\n", dist[i]);
    }

    return 0;
}