#include <string>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int answer = 0;
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
vector<vector<vector<int>>> visited;

bool inRange(int x, int y, int n) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

void BFS(int n, vector<vector<int>> board) {
    queue<tuple<int, int, int, int, int>> q;
    // (0, 0), (0, 1), time = 0
    q.push({0, 0, 0, 1, 0});

    visited[0][0][0] = 1;

    while(!q.empty()) {
        auto [x1, y1, x2, y2, time] = q.front();
        q.pop();

        if ((x1 == n - 1 && y1 == n - 1) || (x2 == n - 1 && y2 == n - 1)) {
            answer = time;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx1 = x1 + dx[i];
            int ny1 = y1 + dy[i];
            int nx2 = x2 + dx[i];
            int ny2 = y2 + dy[i];

            if (inRange(nx1, ny1, n) && inRange(nx2, ny2, n) && board[nx1][ny1] == 0 && board[nx2][ny2] == 0) {
                int nd = (nx1 == nx2) ? 0 : 1; // 0: 가로, 1: 세로
                int fx = min(nx1, nx2);
                int fy = min(ny1, ny2);
                if (!visited[fx][fy][nd]) {
                    visited[fx][fy][nd] = 1;
                    q.push({nx1, ny1, nx2, ny2, time + 1});
                }
            }
        }


        // 회전
        if (x1 == x2) { // 가로 방향 -> 세로로 회전
            for (int d = -1; d <= 1; d += 2) {
                if (inRange(x1 + d, y1, n) && inRange(x2 + d, y2, n)
                    && board[x1 + d][y1] == 0 && board[x2 + d][y2] == 0) {

                    // x1축 회전
                    int nx1 = x1;
                    int ny1 = y1;
                    int nx2 = x1 + d;
                    int ny2 = y1;
                    int fx = min(nx1, nx2);
                    int fy = min(ny1, ny2);

                    if (!visited[fx][fy][1]) {
                        visited[fx][fy][1] = 1;
                        q.push({nx1, ny1, nx2, ny2, time+1});
                    }

                    // x2축 회전
                    nx1 = x2;
                    ny1 = y2;
                    nx2 = x2 + d;
                    ny2 = y2;
                    fx = min(nx1, nx2);
                    fy = min(ny1, ny2);

                    if (!visited[fx][fy][1]) {
                        visited[fx][fy][1] = 1;
                        q.push({nx1, ny1, nx2, ny2, time+1});
                    }
                }
            }
        } else if (y1 == y2) { // 세로 방향 -> 가로로 회전
            for (int d = -1; d <= 1; d += 2) {
                if (inRange(x1, y1 + d, n) && inRange(x2, y2 + d, n)
                    && board[x1][y1 + d] == 0 && board[x2][y2 + d] == 0) {

                    // y1축 회전
                    int nx1 = x1;
                    int ny1 = y1;
                    int nx2 = x1;
                    int ny2 = y1 + d;
                    int fx = min(nx1, nx2);
                    int fy = min(ny1, ny2);

                    if (!visited[fx][fy][0]) {
                        visited[fx][fy][0] = 1;
                        q.push({nx1, ny1, nx2, ny2, time+1});
                    }

                    // y2축 회전
                    nx1 = x2;
                    ny1 = y2;
                    nx2 = x2;
                    ny2 = y2 + d;
                    fx = min(nx1, nx2);
                    fy = min(ny1, ny2);

                    if (!visited[fx][fy][0]) {
                        visited[fx][fy][0] = 1;
                        q.push({nx1, ny1, nx2, ny2, time+1});
                    }
                }
            }
        }
    }
}

int solution(vector<vector<int>> board) {
    int n = board.size();
    // x, y, nd
    visited.assign(n, vector<vector<int>> (n, vector<int>(2, 0)));


    BFS(n, board);
    return answer;
}