// 프로그래머스 외벽 점검 수열
#include <string>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> weak, vector<int> dist) {
    int r = INT_MAX;
    int len = weak.size();
    for (int i = 0; i < len; i++) {
        weak.push_back(weak[i] + n);
    }

    sort(dist.begin(), dist.end());
    bool isFirst = true; // 첫 번째 시작
    while (isFirst || next_permutation(dist.begin(), dist.end())) {
        isFirst = false;
        for (int i = 0; i < len; i++) {
            int friendIdx = 0; // 현재 투입할 친구
            int maxCover = weak[i] + dist[friendIdx]; // 현재 친구가 커버할 수 있는 최대 거리

            bool allCovered = true;
            // 출발점부터 len개의 취약지점을 차례로 점검
            for (int j = i; j < i + len; j++) {
                if (weak[j] > maxCover) {
                    friendIdx++;
                    // 더 이상 친구가 없음 -> 커버 실패
                    if (friendIdx >= dist.size()) {
                        allCovered = false;
                        break;
                    }
                    maxCover = weak[j] + dist[friendIdx];
                }
            }

            if (allCovered) {
                r = min(r, friendIdx + 1);
            }
        }
    }
    return (r == INT_MAX) ? -1 : r;
}