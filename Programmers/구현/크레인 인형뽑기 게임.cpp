#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int n = board.size();
    vector<int> stack;

    for (auto move : moves) {
        for (int i = 0; i < n; i++) {
            int tmp = board[i][move - 1];
            if (tmp != 0) {
                if (!stack.empty() && stack.back() == tmp) {
                    stack.pop_back();
                    answer += 2;
                } else {
                    stack.push_back(tmp);
                }
                board[i][move - 1] = 0;
                break;
            }
        }
    }

    return answer;
}