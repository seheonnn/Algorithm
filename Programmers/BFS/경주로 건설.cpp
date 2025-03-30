// 프로그래머스 경주로 건설 BFS
#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>

using namespace std;

int n;
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
vector<vector<vector<int>>> visited;
void BFS(int x, int y, vector<vector<int>> board) {
    queue<tuple<int, int, int, int>> q;
    q.push({x, y, -1, 0}); // 초기에 방향 설정 X

    while(!q.empty()) {
        auto [x, y, last, cost] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || n <= nx || ny < 0 || n <= ny) continue;

            int newCost = cost + ((last == -1 || last == i) ? 100 : 600);
            if (visited[nx][ny][i] > newCost && board[nx][ny] == 0) {
                visited[nx][ny][i] = newCost;
                q.push({nx, ny, i, newCost});
            }
        }
    }
}
int solution(vector<vector<int>> board) {
    n = board.size();
    visited.assign(n, vector<vector<int>>(n, vector<int>(4, INT_MAX)));

    BFS(0, 0, board);

    int r = INT_MAX;
    for (int i = 0; i < 4; i++) {
        r = min(r, visited[n - 1][n - 1][i]);
    }
    return r;
}