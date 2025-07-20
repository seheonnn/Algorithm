#include <string>
#include <vector>
#include <queue>

using namespace std;

int r = 0;
vector<vector<int>> graph;

void DFS(int cur, int sheep, int wolf, vector<int> info, vector<int> next_nodes) {
    if (info[cur] == 0) sheep++;
    else wolf++;

    if (wolf >= sheep) return;

    r = max(r, sheep);

    vector<int> candidates = next_nodes;

    for (int next : graph[cur]) {
        candidates.push_back(next);
    }

    for (int i = 0; i < candidates.size(); i++) {
        vector<int> next = candidates;          // 현재 후보 노드 리스트 복사
        next.erase(next.begin() + i);           // 이번에 방문할 노드는 후보에서 제거
        DFS(candidates[i], sheep, wolf, info, next);  // 선택한 노드로 DFS 수행
    }
}

int solution(vector<int> info, vector<vector<int>> edges) {
    int answer = 0;
    int n = info.size();

    graph.assign(n, vector<int>());

    for (auto tmp : edges) {
        graph[tmp[0]].push_back(tmp[1]);
    }

    DFS(0, 0, 0, info, {});

    return r;
}