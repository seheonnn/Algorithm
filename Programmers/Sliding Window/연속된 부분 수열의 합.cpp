// 프로그래머스 연속된 부분 수열의 합 슬라이딩윈도우
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {

    int n = sequence.size();
    int start = 0, end = 0;
    int sum = sequence[0];
    vector<int> answer = {0, n - 1};

    while (start <= end && end < n) {
        if (sum < k) {
            end++;
            if (end < n) {
                sum +=sequence[end];
            }
        } else if (sum > k) {
            sum -= sequence[start];
            start++;
        } else { // sum == k인 경우
            if (answer[1] - answer[0] > end - start) {
                answer[0] = start;
                answer[1] = end;
            }
            sum -= sequence[start];
            start++;

        }
    }

    return answer;
}