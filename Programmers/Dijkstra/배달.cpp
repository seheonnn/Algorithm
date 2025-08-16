#include <iostream>
#include <vector>
#include <climits>
#include <queue>

using namespace std;

vector<vector<pair<int, int>>> graph;
vector<int> dist;

void Dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push({dist[start], start});

    while (!pq.empty()) {
        auto [d, cur]  = pq.top();
        pq.pop();

        for (auto [next, w] : graph[cur]) {
            int new_dist = w + d;
            if (dist[next] > new_dist) {
                dist[next] = new_dist;
                pq.push({new_dist, next});
            }
        }
    }
}

int solution(int n, vector<vector<int> > road, int k) {
    int answer = 0;
    graph.assign(n + 1, vector<pair<int, int>>());
    dist.assign(n + 1, INT_MAX);

    for (auto tmp : road) {
        int a = tmp[0];
        int b = tmp[1];
        int c = tmp[2];
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    Dijkstra(1);

    for (auto num : dist) {
        if (num <= k) answer++;
    }

    return answer;
}