#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> visited;
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};
int n, m;

void BFS(int x, int y, vector<string>& board) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = 0;

    while(!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        if (board[x][y] == 'G') return;

        for (int i = 0; i < 4; i++) {

            int nx = x;
            int ny = y;

            while(true) {
                int tx = nx + dx[i];
                int ty = ny + dy[i];

                if (tx < 0 || n <= tx || ty < 0 || m <= ty || board[tx][ty] == 'D') break;

                nx = tx;
                ny = ty;
            }
            if (visited[nx][ny] == -1) {
                visited[nx][ny] = visited[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
}

int solution(vector<string> board) {

    int startX, startY, goalX, goalY;
    n = board.size();
    m = board[0].size();
    visited.assign(n, vector<int>(m, -1));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 'R') {
                startX = i; startY = j;
            } else if (board[i][j] == 'G') {
                goalX = i; goalY = j;
            }
        }
    }

    BFS(startX, startY, board);

    return visited[goalX][goalY];
}