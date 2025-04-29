// 프로그래머스 징검다리 건너기 이분탐색
#include <string>
#include <vector>

using namespace std;

bool canCross(vector<int> stones, int k, int mid) {
    int cnt = 0;
    for (int stone : stones) {
        if (stone < mid) {
            cnt++;
            if (cnt >= k) return false;
        } else {
            cnt = 0; // 연속이 아니라면 초기화
        }
    }
    return true;
}

int solution(vector<int> stones, int k) {
    int answer = 0;
    int left = 1, right = 1;

    for (int i = 0; i < stones.size(); i++) {
        right = max(right, stones[i]);
    }

    while (left <= right) {
        int mid = (left + right) / 2;
        if (canCross(stones, k, mid)) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return answer;
}