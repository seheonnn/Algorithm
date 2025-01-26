#include <iostream>
#include <vector>
#include <queue>

#define MAX 100000

using namespace std;

int n;
int visited[MAX];
vector<int> graph[MAX];

 void BFS(int v) {
     queue<int> q;
     q.push(v);
     while(!q.empty()) {
         int cur = q.front();
         q.pop(); // pop_front()는 반환값 없이 pop만
         for (int child : graph[cur]) {
             if (visited[child] == 0) {
                 visited[child] = cur;
                 q.push(child);
             }
         }
     }
 }

//void DFS(int v) {
//    for (int child : graph[v]) {
//        if (visited[child] == 0) {
//            visited[child] = v;
//            DFS(child);
//        }
//    }
//}

int main() {
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].emplace_back(b);
        graph[b].emplace_back(a);
    }

    visited[1] = 1;
    BFS(1);
    for (int i = 2; i < n + 1; i++) {
        cout << visited[i] << "\n";
    }
    return 0;
}
