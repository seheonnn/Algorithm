#include <iostream>
#include <vector>
#include <deque>

#define MAX 100000

using namespace std;

int n;
int visited[MAX];
vector<int> graph[MAX];

// void BFS(int v) {
//     deque<int> queue;
//     queue.push_back(v);
//     while(!queue.empty()) {
//         int cur = queue.front();
//         queue.pop_front(); // pop_front()는 반환값 없이 pop만
//         for (int child : graph[cur]) {
//             if (visited[child] == 0) {
//                 visited[child] = cur;
//                 queue.push_back(child);
//             }
//         }
//     }
// }

void DFS(int v) {
    for (int child : graph[v]) {
        if (visited[child] == 0) {
            visited[child] = v;
            DFS(child);
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].emplace_back(b);
        graph[b].emplace_back(a);
    }

    visited[1] = 1;
    DFS(1);
    for (int i = 2; i < n + 1; i++) {
        cout << visited[i] << "\n";
    }
    return 0;
}