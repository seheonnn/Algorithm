#include <string>
#include <vector>
#include <queue>
using namespace std;

vector<int> visited;

void BFS(int v, int n, vector<vector<int>> computers) {
    priority_queue<int> pq;
    pq.push(v);

    while(!pq.empty()) {
        v = pq.top();
        pq.pop();

        for (int next = 0; next < n; next++) {
            if (computers[v][next] == 1 && visited[next] == 0) {
                visited[next] = 1;
                pq.push(next);
            }
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    visited.assign(n, 0);
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            BFS(i, n, computers);
            answer++;
        }
    }
    return answer;
}