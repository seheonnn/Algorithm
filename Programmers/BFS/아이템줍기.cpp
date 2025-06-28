#include <string>
#include <vector>
#include <cstring>
#include <queue>

#define MAX 101

using namespace std;

int graph[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};
int answer = 0;

void BFS(int x, int y, int itemX, int itemY) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = 1;

    while(!q.empty()) {
        auto tmp = q.front();
        x = tmp.first;
        y = tmp.second;
        q.pop();

        if (x == itemX && y == itemY) {
            answer = visited[x][y] / 2;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || MAX <= nx || ny < 0 || MAX <= ny) continue;
            if (graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                visited[nx][ny] = visited[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    memset(graph, -1, sizeof(graph));

    for (auto& tmp : rectangle) {

        // 겹치는 테두리를 정확히 구분하기 위함
        int x1 = tmp[0] * 2;
        int y1 = tmp[1] * 2;
        int x2 = tmp[2] * 2;
        int y2 = tmp[3] * 2;

        // 범위 주의
        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                if (x1 < i && i < x2 && y1 < j && j < y2) graph[i][j] = 0; // 직사각형 내부인 경우
                else if (graph[i][j] != 0) graph[i][j] = 1;
            }
        }
    }


    BFS(characterX * 2, characterY * 2, itemX * 2, itemY * 2);

    return answer;
}