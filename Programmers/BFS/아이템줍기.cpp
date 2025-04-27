// 프로그래머스 아이템줍기 BFS
#include <vector>
#include <deque>

using namespace std;

int graph[101][101];
int visited[101][101];
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
int answer;

void BFS(int x, int y, int ix, int iy) {
    deque<pair<int, int>> queue;
    queue.push_back({x, y});

    while(!queue.empty()) {
        x = queue.front().first;
        y = queue.front().second;
        queue.pop_front();

        if (x == ix && y == iy) {
            answer = visited[ix][iy]  / 2;
            return;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || 101 <= nx || ny < 0 || 101 <= ny) continue;
            if (graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                visited[nx][ny] = visited[x][y] + 1;
                queue.push_back({nx, ny});
            }
        }
    }
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {

    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++) {
            graph[i][j] = -1;
        }
    }

    for (auto tmp : rectangle) {
        int x1 = tmp[0] * 2;
        int y1 = tmp[1] * 2;
        int x2 = tmp[2] * 2;
        int y2 = tmp[3] * 2;

        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                if (x1 < i && i < x2 && y1 < j && j < y2) {
                    graph[i][j] = 0;
                } else if (graph[i][j] != 0) {
                    graph[i][j] = 1;
                }
            }
        }
    }

    visited[characterX * 2][characterY * 2] = 1;
    BFS(characterX * 2, characterY * 2, itemX * 2, itemY * 2);

    return answer;
}