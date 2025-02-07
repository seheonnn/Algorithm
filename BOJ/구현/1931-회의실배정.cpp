// 백준 1931 회의실 배정 구현
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
   int n;
   cin >> n;

   vector<pair<int, int>> time;

   for (int i = 0; i < n; i++) {
      int s, e;
      cin >> s >> e;
      time.push_back({ e, s }); // 끝나는 시간 기준으로 sort 해야 하므로 반대로 저장
   }

   sort(time.begin(), time.end());

   int last = 0;
   int cnt = 0;

   for (auto tmp : time) {
      int s = tmp.second;
      int e = tmp.first;
      if (s >= last) {
         cnt++;
         last = e;
      }
   }

   cout << cnt << "\n" ;
}