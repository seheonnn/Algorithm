// 프로그래머스 연속 펄스 부분 수열의 합 부분합 카데인 알고리즘
#include <string>
#include <vector>

using namespace std;

long long solution(vector<int> sequence) {
    long long answer = 0;
    int n = sequence.size();
    vector<long long> pulse1(n), pulse2(n);

    for (int i = 0; i < n; i++) {
        pulse1[i] = sequence[i] * (i % 2 == 0 ? 1 : -1);
        pulse2[i] = sequence[i] * (i % 2 == 0 ? -1 : 1);
    }

    long long max_sum1 = pulse1[0], cur_sum1 = pulse1[0];
    long long max_sum2 = pulse2[0], cur_sum2 = pulse2[0];

    for (int i = 1; i < n; i++) {
        cur_sum1 = max(pulse1[i], cur_sum1 + pulse1[i]);
        max_sum1 = max(max_sum1, cur_sum1);

        cur_sum2 = max(pulse2[i], cur_sum2 + pulse2[i]);
        max_sum2 = max(max_sum2, cur_sum2);
    }

    return max(max_sum1, max_sum2);
}