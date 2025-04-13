// 백준 16933 벽 부수고 이동하기 3
#include <iostream>
#include <vector>
#include <tuple>
#include <deque>

using namespace std;

int n, m, k;
vector<vector<int>> graph;
vector<vector<vector<int>>> visited;
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
int r = -1;

void BFS(int x, int y, int wall, int day) {
    deque<tuple<int, int, int, bool>> queue;
    queue.push_back({ x, y, wall, day });

    while(!queue.empty()) {
        auto [x, y, wall, day] = queue.front();
        queue.pop_front();

        if (x == n - 1 && y == m - 1) {
            r = visited[x][y][wall];
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || n <= nx || ny < 0 || m <= ny) continue;
            if (graph[nx][ny] == 0 && visited[nx][ny][wall] == 0) {
                visited[nx][ny][wall] = visited[x][y][wall] + 1;
                queue.push_back({ nx, ny, wall, !day });
            } else if (graph[nx][ny] == 1 && wall < k && day && visited[nx][ny][wall + 1] == 0) {
                visited[nx][ny][wall + 1] = visited[x][y][wall] + 1;
                queue.push_back({ nx, ny, wall + 1, !day });
            }
        }

        if (!day) { // for 0 ~ 4 밖에서 밤낮 바꿔야
            visited[x][y][wall] = visited[x][y][wall] + 1;
            queue.push_back({x, y, wall, true});
        }
    }
}

int main() {
    cin >> n >> m >> k;
    graph.assign(n, vector<int>(m));
    visited.assign(n, vector<vector<int>>(m, vector<int>(k + 1, 0)));


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            char tmp;
            cin >> tmp;
            graph[i][j] = tmp - '0';
        }
    }
    visited[0][0][0] = 1;
    BFS(0, 0, 0, true);

    cout << r << endl;

    return 0;
}