// 프로그래머스 가장 먼 노드 BFS
#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> graph;
vector<int> visited;
void BFS(int v) {
    queue<int> q;
    q.push(v);

    while(!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int next : graph[cur]) {
            if (visited[next] == 0) {
                visited[next] = visited[cur] + 1;
                q.push(next);
            }
        }
    }
}

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    graph.assign(n + 1, vector<int>());
    visited.assign(n + 1, 0);

    for (auto tmp : edge) {
        graph[tmp[0]].push_back(tmp[1]);
        graph[tmp[1]].push_back(tmp[0]);
    }

    visited[1] = 1;
    BFS(1);

    int maxDis = 0;
    for (int i = 1; i <= n; i++) {
        maxDis = max(maxDis, visited[i]);
    }

    for (int i = 1; i <= n; i++) {
        if (visited[i] == maxDis) answer++;
    }

    return answer;
}