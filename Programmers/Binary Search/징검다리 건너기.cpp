#include <string>
#include <vector>

using namespace std;

bool canCross(vector<int>& stones, int k, int mid) {
    int cnt = 0; // 건너뛰는 돌 수
    for (int stone : stones) {
        if (stone < mid) {
            cnt++;
            if (cnt >= k) return false;
        } else {
            cnt = 0; // 디딤돌값이 mid보다 크면 밟아도 됨
        }
    }
    return true;
}

int solution(vector<int> stones, int k) {
    int answer = 0;

    int left = 1, right = 1;
    for (int i = 0; i < stones.size(); i++) {
        // 건널 수 있는 사람 수의 범위 1 ~ stones 배열의 최댓값
        right = max(right, stones[i]);
    }

    while(left <= right) {
        int mid = (left + right) / 2; // 건널 수 있는 사람 수

        if (canCross(stones, k, mid)) { // mid 명이 건널 수 있다면
            // 답 갱신 후 더 많은 인원으로 검사
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return answer;
}