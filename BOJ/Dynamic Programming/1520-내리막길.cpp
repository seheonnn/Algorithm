// 백준 1520 dp + DFS
#include <iostream>
#include <vector>

using namespace std;

int m, n;
vector<vector<int>> graph;
vector<vector<int>> dp;
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};

int dfs(int x, int y) {

    if (x == m - 1 && y == n - 1) return 1;
    if (dp[x][y] != -1) return dp[x][y];
    dp[x][y] = 0;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || m <= nx || ny < 0 || n <= ny) continue;
        if (graph[x][y] > graph[nx][ny]) {
            dp[x][y] += dfs(nx, ny);
        }
    }
    return dp[x][y];
}

int main() {
    cin >> m >> n;
    graph.assign(m, vector<int> (n, 0));
    dp.assign(m, vector<int> (n, -1));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
        }
    }

    cout << dfs(0, 0) << "\n";

    return 0;
}