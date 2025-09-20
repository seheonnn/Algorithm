#include <vector>
#include <queue>

using namespace std;

int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};

int BFS(int x, int y, int m, int n, vector<vector<int>>& picture, vector<vector<bool>>& visited) {
    int cnt = 1;
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;

    while(!q.empty()) {
        auto tmp = q.front();
        q.pop();
        x = tmp.first;
        y = tmp.second;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || m <= nx || ny < 0 || n <= ny) continue;
            if (!visited[nx][ny] && picture[nx][ny] == picture[x][y]) {
                visited[nx][ny] = true;
                cnt++;
                q.push({nx, ny});
            }
        }
    }
    return cnt;

}
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    vector<vector<bool>> visited(m, vector<bool>(n));
    vector<int> r;
    int maxSize = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j] && picture[i][j] != 0) {
                int tmp = BFS(i,j, m, n, picture, visited);
                maxSize = maxSize < tmp ? tmp : maxSize;
                r.push_back(tmp);
            }
        }
    }

    vector<int> answer(2);
    answer[0] = r.size();
    answer[1] = maxSize;
    return answer;
}