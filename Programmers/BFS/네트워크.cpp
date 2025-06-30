#include <string>
#include <vector>
#include <queue>

using namespace std;

// 110
// 110
// 001

vector<bool> visited(3);
void BFS(int start, int n, vector<vector<int>> computers) {
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for (int i = 0; i < n; i++) {
            if (!visited[i] && computers[v][i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            BFS(i, n, computers);
            answer++;
        }
    }
    return answer;
}