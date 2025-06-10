






나의 말:
#include <string>
#include <vector>

using namespace std;

bool isWin(vector<string>& board, char player) {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true;
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return true;
    }

    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true;

    return false;
}

int solution(vector<string> board) {

    int oCnt = 0;
    int xCnt = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == 'O') oCnt++;
            else if (board[i][j] == 'X') xCnt++;
        }
    }

    bool oWin = isWin(board, 'O');
    bool xWin = isWin(board, 'X');

    if (oWin && xWin) return 0;
    if (xCnt > oCnt || oCnt - xCnt > 1) return 0;
    if (oWin && (oCnt <= xCnt)) return 0;
    if (xWin && (oCnt != xCnt)) return 0;

    return 1;
}