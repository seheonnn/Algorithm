// 코드트리 방화벽 설치하기 BFS, 백트래킹
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<int>> graph;
int r = 0;
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};

void BFS(vector<vector<int>>& graph) {
    queue<pair<int, int>> q;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 2) {
                q.push({i, j});
            }
        }
    }

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            if (graph[nx][ny] == 0) {
                graph[nx][ny] = 1;
                q.push({nx, ny});
            }
        }
    }
}

int countSafe(vector<vector<int>>& graph) {
    int cnt = 0;
    for (auto rows : graph) {
        for (auto val : rows) {
            if (val == 0) {
                cnt++;
            }
        }
    }
    return cnt;
}

void backtracking(int wall) {
    if (wall == 3) {
        vector<vector<int>> tmp = graph;
        BFS(tmp);
        r = max(r, countSafe(tmp));
        return;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 0) {
                graph[i][j] = 1;
                backtracking(wall + 1);
                graph[i][j] = 0;
            }
        }
    }
}

int main() {
    cin >> n >> m;

    graph.assign(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> graph[i][j];
        }
    }

    backtracking(0);
    cout << r << endl;

    return 0;
}