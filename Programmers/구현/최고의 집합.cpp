// 프로그래머스 최고의 집합
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer(n, 0);

    int num = s / n;
    int rst = s % n;

    if (num == 0) {
        return {-1};
    }

    for (int i = 0; i < n; i++) {
        answer[i] = num;
    }

    int idx = n - 1;
    while (rst--) {
        answer[idx--] += 1; // 뒤에서부터 채워 sort를 사용하지 않음
    }

    // sort(answer.begin(), answer.end());

    return answer;
}