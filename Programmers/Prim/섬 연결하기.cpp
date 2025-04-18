// 프로그래머스 섬 연결하기 프림 알고리즘(MST 최소 신장 트리)
#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<vector<pair<int, int>>> graph;
vector<int> visited;

int prim(int n, int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    int totalCost = 0;
    int usedEdge = 0;

    while (!pq.empty()) {
        int d = pq.top().first;
        int v = pq.top().second;
        pq.pop();

        if (visited[v]) continue;  // 이미 방문한 노드는 스킵

        visited[v] = 1;  // 방문 체크 (여기가 중요)
        totalCost += d;
        usedEdge++;

        for (auto [next, w] : graph[v]) {
            if (!visited[next]) {
                pq.push({w, next});
            }
        }
    }

    return totalCost;
}

int solution(int n, vector<vector<int>> costs) {
    graph.assign(n, vector<pair<int, int>>());
    visited.assign(n, 0);

    for (vector<int> tmp : costs) {
        graph[tmp[0]].push_back({tmp[1], tmp[2]});
        graph[tmp[1]].push_back({tmp[0], tmp[2]});
    }

    return prim(n, 0);
}
