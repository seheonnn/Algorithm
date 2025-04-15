#include <iostream>
#include <string>
#include <vector>
#include <climits>

using namespace std;
// 0 : 다이아몬드, 1 : 철, 2 : 돌
vector<vector<int>> arr = {{1, 1, 1}, {5, 1, 1}, {25, 5, 1}};
int answer = INT_MAX;
void backtracking(vector<int> picks, vector<string> minerals, int idx, int cnt) {
    if (idx >= minerals.size() || (picks[0] == 0 && picks[1] == 0 && picks[2] == 0)) { // 다 캤거나 광물이 없을 때 종료
        answer = min(answer, cnt);
        return;
    }

    for (int i = 0; i < 3; i++) {
        if (picks[i] > 0) {
            int cur = 0;
            picks[i]--;
            for (int j = idx; j < min(idx + 5, (int) minerals.size()); j++) { // 주의 !!
                if (minerals[j] == "diamond") cur += arr[i][0];
                else if (minerals[j] == "iron") cur += arr[i][1];
                else if (minerals[j] == "stone") cur += arr[i][2];

            }
            backtracking(picks, minerals, idx + 5, cnt + cur);
            picks[i]++;
        }

    }
}

int solution(vector<int> picks, vector<string> minerals) {
    backtracking(picks, minerals, 0, 0);
    return answer;
}