// 백준 9663 N-Queen 백트래킹
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, cnt;
vector<int> board; // i행에 퀸이 배치된 열 board[i]

// 현재 퀸을 row에 놓을 때 비교
bool isPoss(int row) {
   for (int i = 0; i < row;i++) {
      // 이전에 놓은 i와 같은 열이면 안 됨 or i와 같은 대각선상에 있으면 안 됨 (직접 그려보기)
      if (board[row] == board[i] or row - i == abs(board[row] - board[i])) {
         return false;
      }
   }
   return true;
}

void backtracking(int row) {
   if (row == n) {
      cnt++;
      return;
   }

   for (int i = 0; i < n;i++) {
      board[row] = i;
      if (isPoss(row)) {
         // 동일한 row를 호출하지 않기 때문에 row != i인지 확인할 필요 X
         backtracking(row + 1);
      }
   }
}

int main() {
   cin >> n;

   board.resize(n, 0);
   backtracking(0);

   cout << cnt;
   return 0;
}