// 프로그래머스 숫자 게임 투 포인터
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int solution(vector<int> A, vector<int> B) {
    int answer = 0;

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    int i = 0;
    int j = 0;
    while (i < A.size() && j < B.size()) {
        if (B[j] > A[i]) {
            answer++;
            i++;
        }
        j++;
    }
    return answer;
}