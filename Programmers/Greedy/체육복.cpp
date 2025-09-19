#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    vector<int> students(n + 2, 1);

    // 도난당한 학생은 체육복 -1
    for (int l : lost) {
        students[l]--;
    }

    // 여벌이 있는 학생은 체육복 +1
    for (int r : reserve) {
        students[r]++;
    }

    // 앞 또는 뒤에서 빌릴 수 있는 경우 처리
    for (int i = 1; i <= n; i++) {
        if (students[i] == 0) {
            if (students[i - 1] == 2) {
                students[i]++;
                students[i - 1]--;
            } else if (students[i + 1] == 2) {
                students[i]++;
                students[i + 1]--;
            }
        }
    }

    // 체육복이 있는 학생 수 세기
    int answer = 0;
    for (int i = 1; i <= n; i++) {
        if (students[i] > 0) answer++;
    }

    return answer;
}

