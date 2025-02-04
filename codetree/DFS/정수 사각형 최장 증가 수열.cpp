// 코드트리 정수 사각형 최장 증가 수열 DFS
#include <iostream>

using namespace std;

int n;
int grid[500][500];
int dp[500][500];

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

void dfs(int x, int y) {

    // 이미 계산된 값이 있으면
    if (dp[x][y] != -1) {
        return;
    }

    dp[x][y] = 1; // 현재 위치의 LIS 길이는 최소 1

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 or n <= nx or ny < 0 or n <= ny) {
            continue;
        }

        if (grid[nx][ny] > grid[x][y]) {
            dfs(nx, ny);
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1);
        }
    }
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            dp[i][j] = -1;
        }
    }

    int r = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dfs(i, j);
            r = max(r, dp[i][j]);
        }
    }

    cout << r << endl;

    return 0;
}
