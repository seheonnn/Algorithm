// 백준 20040  사이클 게임 집합
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, cycle;
vector<int> set;

int find(int a) {
    if (set[a] != a) {
        set[a] = find(set[a]);
    }
    return set[a];
}

void unionCus(int a, int b) {
    a = find(a);
    b = find(b);

    if (a != b) {
        set[b] = a;
    }
}

bool isCycle(int a, int b) {
    return find(a) == find(b);
}

int main() {
    scanf("%d %d", &n, &m);
    set.resize(n);
    cycle = 0;

    for (int i = 0; i < n; i++) {
        set[i] = i;
    }

    for (int i = 1; i <= m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);

        if (isCycle(u, v) && cycle == 0) { // 처음 사이클이 생기는 지점 == 이미 같은 집합인데 연결하려 함
            cycle = i;
        }

        unionCus(u, v);
    }

    printf("%d\n", cycle);
}