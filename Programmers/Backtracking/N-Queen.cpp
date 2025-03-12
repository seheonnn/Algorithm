#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> board;
int cnt;

bool isPoss(int row) {
    for (int i = 0; i < row; i++) {
        if (board[row] == board[i] || row - i == abs(board[row] - board[i])) {
            return false;
        }
    }
    return true;
}

void backtracking(int row, int n) {
    if (row == n) {
        cnt++;
        return;
    }

    for (int i = 0; i < n; i++) {
        board[row] = i;
        if (isPoss(row)) {
            backtracking(row + 1, n);
        }
    }
}

int solution(int n) {
    board.assign(n, 0);
    backtracking(0, n);
    return cnt;
}