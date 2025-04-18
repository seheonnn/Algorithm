// 프로그래머스 섬 연결하기 크루스칼 알고리즘(MST 최소 신장 트리)
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, pair<int, int>>> tree;
vector<int> parents;

int find(int a) {
    if (a != parents[a]) {
        parents[a] = find(parents[a]); // 경로 압축
    }
    return parents[a];
}

void unionCus(int a, int b) {
    a = find(a);
    b = find(b);

    if (a < b) {
        parents[b] = a;
    } else {
        parents[a] = b;
    }
}

int solution(int n, vector<vector<int>> costs) {
    parents.assign(n, 0);

    for (vector<int> tmp : costs) {
        tree.push_back({tmp[2], {tmp[0], tmp[1]}});
        tree.push_back({tmp[2], {tmp[1], tmp[0]}});
    }

    for (int i = 0; i < n; i++) {
        parents[i] = i;
    }

    sort(tree.begin(), tree.end());

    int totalCost = 0;
    int usedEdge  = 0;
    for (auto tmp : tree) {
        int cost = tmp.first;
        int from = tmp.second.first;
        int to = tmp.second.second;

        if (find(from) != find(to)) {
            unionCus(from, to);
            totalCost += cost;
            usedEdge++;
        }

        if (usedEdge == n - 1) break;
    }

    return totalCost;
}
