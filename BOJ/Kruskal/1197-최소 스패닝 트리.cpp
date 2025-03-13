// 백준 1197 최소 스패닝 트리 크루스칼

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int v, e;
vector<tuple<int, int, int>> graph;
vector<int> parents;

int find(int a) {
    if (parents[a] == a) {
        return a;
    }
    return parents[a] = find(parents[a]);
}

void unionCus(int a, int b) {
    a = find(a);
    b = find(b);

    if (a != b) parents[b] = a;
}

int kruskal() {
    sort(graph.begin(), graph.end());
    int r = 0, cnt = 0;
    for (auto [c, a, b] : graph) {
        if (find(a) != find(b)) {
            unionCus(a, b);
            r += c;
            cnt++;
            if (cnt == v - 1) break;
        }
    }
    return r;
}

int main() {
    cin >> v >> e;
    parents.assign(v + 1, 0);
    for (int i = 0; i <= v; i++) {
        parents[i] = i;
    }

    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph.push_back({c, a, b});
    }

    cout << kruskal() << endl;

    return 0;
}