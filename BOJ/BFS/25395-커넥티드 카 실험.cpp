// 백준 25395 커넥티드 카 실험 BFS
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, s;
vector<int> x, h, visited;

void BFS(int v) {
    queue<int> q;
    q.push(v);

    while(!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int left = cur - 1; left >= 0 && x[cur] - x[left] <= h[cur]; left--) {
            if (visited[left] == 0) {
                visited[left] = 1;
                q.push(left);
            }
        }

        for (int right = cur + 1; right < n && x[right] - x[cur] <= h[cur]; right++) {
            if (visited[right] == 0) {
                visited[right] = 1;
                q.push(right);
            }
        }
    }
}

int main() {
    cin >> n >> s;
    x.assign(n, 0);
    h.assign(n, 0);
    visited.assign(n, 0);

    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }

    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }

    visited[s - 1] = 1;
    BFS(s - 1);
    for (int i = 0; i < n; i++) {
        if (visited[i] == 1) {
            cout  << i + 1 << " ";
        }
    }

    return 0;
}