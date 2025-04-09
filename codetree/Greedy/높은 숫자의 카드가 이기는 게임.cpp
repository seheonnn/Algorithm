#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> B(N);
    set<int> A;

    // 전체 카드: 1부터 2N까지
    for (int i = 1; i <= 2 * N; i++) {
        A.insert(i);
    }

    // B의 카드 입력 받고 A에서 제거
    for (int i = 0; i < N; i++) {
        cin >> B[i];
        A.erase(B[i]);
    }

    int score = 0;

    for (int i = 0; i < N; i++) {
        int b = B[i];
        // A에서 b보다 큰 값 중 가장 작은 값 찾기
        auto it = A.upper_bound(b);
        if (it != A.end()) {
            score++;
            A.erase(it);  // 사용한 카드 제거
        } else {
            // 이길 카드 없으면 가장 작은 거 버리기
            A.erase(A.begin());
        }
    }

    cout << score << endl;
    return 0;
}
