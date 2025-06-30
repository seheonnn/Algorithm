#include <string>
#include <vector>
#include <queue>

using namespace std;

void BFS(int v, int n, vector<vector<int>>& graph, vector<int>& visited) {
    queue<int> q;
    q.push(v);
    visited[v] = 1;

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
    vector<vector<int>> graph(n + 1, vector<int> ());
    vector<int> visited(n + 1, 0);

    for (auto tmp : edge) {
        graph[tmp[0]].push_back(tmp[1]);
        graph[tmp[1]].push_back(tmp[0]);
    }

    BFS(1, n, graph, visited);
    int maxLen = 0;
    for (int i = 1; i <= n; i++) {
        if (maxLen < visited[i]) maxLen = visited[i];
    }

    for (int i = 1; i <= n; i++) {
        if (maxLen == visited[i]) answer++;
    }

    return answer;
}