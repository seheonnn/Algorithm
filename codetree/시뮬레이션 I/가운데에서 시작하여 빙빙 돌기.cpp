#include <iostream>
#include <vector>

using namespace std;

int n, x, y;
vector<vector<int>> graph;
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
int nd = 0;
int main() {
    cin >> n;
    graph.assign(n, vector<int>(n));
    x = n - 1;
    y = n - 1;
    for (int i = n * n; i > 0; i--) {
        graph[x][y] = i;
        int nx = x + dx[nd];
        int ny = y + dy[nd];
        if (nx < 0 || n <= nx || ny < 0 || n <= ny || graph[nx][ny] != 0) {
            nd = (nd + 1) % 4;
            x = x + dx[nd];
            y = y + dy[nd];
        } else {
            x = nx;
            y = ny;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
