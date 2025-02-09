// 백준 15651 N과 M (3) 수열
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> answer;
//vector<int> visited; // 중복 체크 필요없음

void backtracking() {
   if (answer.size() == m) {
      for (int num : answer) {
         cout << num << " ";
      }
      cout << "\n";
      return; // return 누락 주의!!
   }

   for (int i = 1; i <= n; i++) {
      answer.push_back(i);
      backtracking();
      answer.pop_back();
   }
}

int main() {
   cin >> n >> m;

   backtracking();
}