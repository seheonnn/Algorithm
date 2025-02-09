// 백준 15652 N과 M (4) 수열
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> answer;

void backtracking(int start) {
   if (answer.size() == m) {
      for (int num : answer) {
         cout << num << " ";
      }
      cout << "\n";
      return;
   }

   for (int i = start; i <= n;i++) {
      answer.push_back(i);
      backtracking(i);
      answer.pop_back();
   }
}

int main() {
   cin >> n >> m;

   backtracking(1);

   return 0;
}