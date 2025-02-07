#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> answer;
vector<int> visited;

void backtracking() {
    if (answer.size() == m) {
        for (int num : answer) {
            cout << num << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 1; i <= n; i++) { // 1부터 N까지 순회
        if (visited[i] == 0) { // 방문하지 않은 숫자만 선택 (중복된 수 피하기)
            visited[i] = 1; // 현재 숫자를 방문 처리
            answer.push_back(i); // 숫자를 수열에 추가
            backtracking(); // 백트래킹 재귀를 통해 answer에 중복되지 않은 수가 쌓임
            // 만약 answer의 길이가 m이 되면 출력하면서 재귀가 끝나고
            answer.pop_back(); // answer에서 숫자 삭제
            visited[i] = 0; // 그리고 사용된 숫자들 방문 삭제
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    visited.resize(n + 1, 0); // n 이 6이라면 visited[6]까지 사용

    backtracking();

    return 0;
}