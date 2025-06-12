#include <vector>
#include <algorithm>
using namespace std;

int r = -1;
vector<int> result;

void calcScore(vector<int> ryan, vector<int> apeach) {
    int rScore = 0, aScore = 0;
    for (int i = 0; i < 11; i++) {
        if (ryan[i] == 0 && apeach[i] == 0) continue;
        if (ryan[i] > apeach[i]) rScore += (10 - i);
        else aScore += (10 - i);
    }
    
    int diff = rScore - aScore;
    if (diff <= 0) return;
    
    if (diff > r) {
        r = diff;
        result = ryan;
    }
    
    else if (diff == r) { // 같은 경우 낮은 점수 더 많이 맞춘 경우로
        for (int i = 10; i >= 0; i--) {
            if (ryan[i] > result[i]) {
                result = ryan;
                break;
            } else if (ryan[i] < result[i]) break;
        }
    }
}

void backtrack(int start, int remain, vector<int>& ryan, vector<int>& apeach) {
    if (remain == 0) {
        calcScore(ryan, apeach);
        return;
    }

    for (int i = start; i < 11; ++i) {
        ryan[i]++;
        backtrack(i, remain - 1, ryan, apeach);
        ryan[i]--;  // 백트래킹
    }
}

vector<int> solution(int n, vector<int> info) {
    vector<int> ryan(11, 0);
    backtrack(0, n, ryan, info);
    if (result.empty()) return {-1};
    return result;
}
