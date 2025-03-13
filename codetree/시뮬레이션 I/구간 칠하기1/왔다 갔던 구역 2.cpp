// 코드트리 왔다 갔던 구역 2 시뮬레이션
#include <iostream>
#define OFFSET 100

using namespace std;

int n;
int graph[201] = {0};
int cur = OFFSET;
int cnt = 0;

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        char c;
        cin >> x >> c;

        for (int j = 0; j < x; j++) {
            int prev = cur;
            if (c == 'L') cur--;
            else if (c == 'R') cur++;

            graph[min(prev, cur)]++;  // 구간 단위
        }
    }

    for (int i = 0; i < 201; i++) {
        if (graph[i] >= 2) {
            cnt++;
        }
    }

    cout << cnt << endl;
    return 0;
}

