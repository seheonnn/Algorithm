#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, int w, int num) {
    int h = (n + w - 1) / w;
    vector<vector<int>> board(h + 1, vector<int>(w + 1));

    int x = h, y = 1, d = 0;
    int goalX = -1, goalY = -1;
    int dy[2] = {1, -1};

    for (int i = 1; i <= n; i++) {
        board[x][y] = i;
        if (i == num) {
            goalX = x;
            goalY = y;
        }

        int ny = y + dy[d];
        if (1 <= ny && ny <= w) {
            y = ny;
        } else {
            d = (d + 1) % 2;
            x -= 1;
        }
    }

    int answer = 0;
    for (int i = 0; i <= h; i++) {
        if (board[i][goalY] != 0) {
            answer++;
            if (board[i][goalY] == num) break;
        }
    }
    return answer;
}
