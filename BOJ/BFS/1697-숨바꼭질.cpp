// 백준 1697 숨바꼭질 BFS
#include <iostream>
#include <deque>
#define MAX 100001

using namespace std;

int n, k;
int visited[MAX];
int r = -1;

void BFS(int v, int t) {
    deque<pair<int ,int>> queue; // 현재 위치, 현재 시간
    queue.push_back({v, t});

    while(!queue.empty()) {
        v = queue.front().first;
        t = queue.front().second;
        queue.pop_front();

        if (v == k) {
            r = t;
        }

        int d[3] = {v + 1, v - 1, 2 * v}; // 이동할 수 있는 경우의 수
        for(int i = 0; i < 3; i++) {
            int nv = d[i];
            if (nv < 0 or MAX <= nv) {
                continue;
            }
            if (visited[nv] == 0) {
                visited[nv] = 1;
                queue.push_back({nv, t + 1});
            }
        }
    }
}

int main() {
    scanf("%d %d", &n, &k);

    visited[n] = 1;
    BFS(n, 0);
    printf("%d\n", r);

    return 0;
}