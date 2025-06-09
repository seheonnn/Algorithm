// 프로그래머스 부대복귀 다익스트라
#include <string>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

vector<vector<int>> graph;
vector<int> dist;

void Dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    dist[start] = 0;
    pq.push({dist[start], start});

    while(!pq.empty()) {
        int d = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if (d > dist[cur]) continue;
        for (int next : graph[cur]) {
            int new_dist = d + 1;
            if (dist[next] > new_dist) {
                dist[next] = new_dist;
                pq.push({dist[next], next});
            }
        }
    }

}

vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer;

    graph.assign(n + 1, vector<int>());
    dist.assign(n + 1, INT_MAX);
    for (auto& tmp : roads) {
        graph[tmp[0]].push_back(tmp[1]);
        graph[tmp[1]].push_back(tmp[0]);
    }

    Dijkstra(destination);

    for (int src : sources) {
        answer.push_back(dist[src] == INT_MAX ? -1 : dist[src]);
    }

    return answer;
}