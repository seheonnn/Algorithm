// 프로그래머스 인사고과 그리디
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int>& a, vector<int>& b) { // 근무 태도 기준 내림차순, 동료 평가 기준 오름차순
    if (a[0] == b[0]) return a[1] < b[1];
    return a[0] > b[0];
}

int solution(vector<vector<int>> scores) {
    int s1 = scores[0][0], s2 = scores[0][1];

    sort(scores.begin(), scores.end(), cmp);
    int maxPeer = 0;
    int rank = 1;

    for (auto tmp : scores) {
        // 이미 근무 태도는 내림차순임, 동료 평가만 비교
        // 나보다 근무 태도 높은 사람 중에, 동료 평가도 나보다 높은 사람이 있었음 → 탈락
        if (tmp[1] < maxPeer) {
            if (tmp[0] == s1 && tmp[1] == s2) { // 자기자신 제외
                return -1;
            }
            continue;
        }

        if (tmp[0] + tmp[1] > s1 + s2) {
            rank++;
        }

        maxPeer = max(maxPeer, tmp[1]); // 동료 평가 최대값 갱신
    }

    return rank;
}