// 백준 1197 최소 스패닝 트리
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 10001

using namespace std;

int parents[MAX];

int find(int v) {
   if (parents[v] != v)
      parents[v] = find(parents[v]);
   return parents[v];
}

void union_a(int a, int b) {
   a = find(a);
   b = find(b);

   if (a < b)
      parents[b] = a;
   else
      parents[a] = b;
}

int main() {
   int v, e;
   cin >> v >> e;

   // 부모 노드 초기화
   for (int i = 1;i <= v;i++) {
      parents[i] = i;
   }

   vector<pair<int, pair<int, int>>> tree;
   for (int i = 0; i < e;i++) {
      int from, to, cost;
      cin >> from >> to >> cost;
      tree.push_back({ cost, {from, to} });
   }

   sort(tree.begin(), tree.end());

   int r = 0;
   for (auto tmp : tree) {
      int cost = tmp.first;
      int from = tmp.second.first;
      int to = tmp.second.second;
      if (find(from) != find(to)) {
         union_a(from, to);
         r += cost;
      }
   }

   cout << r << "\n";
   return 0;
}