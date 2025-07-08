// 프로그래머스 파괴되지 않은 건물 누적합, Imos알고리즘
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int n = board.size();
    int m = board[0].size();

    vector<vector<int>> prefix(n + 1, vector<int>(m + 1, 0));

    for (auto& tmp : skill) {
        int type = tmp[0];
        int r1 = tmp[1], c1 = tmp[2], r2 = tmp[3], c2 = tmp[4], degree = tmp[5];
        int effect = (type == 1) ? -degree : degree;

        prefix[r1][c1] += effect;
        prefix[r1][c2 + 1] -= effect;
        prefix[r2 + 1][c1] -= effect;
        prefix[r2 + 1][c2 + 1] += effect;
    }

    // 가로 방향 누적합: 각 행에서 좌우 누적
    for (int i = 0; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            prefix[i][j] += prefix[i][j - 1];
        }
    }

    // 세로 방향 누적합: 각 열에서 상하 누적
    for (int i = 0; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            prefix[j][i] += prefix[j - 1][i];
        }
    }

    int r = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] + prefix[i][j] > 0) {
                r++;
            }
        }
    }
    return r;
}