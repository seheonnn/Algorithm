// 코드트리 이진수 수열
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> answer;

// cur : 현재 자리
void backtracking(int cur) {
   if (answer.size() == n) {
      for (int num : answer) {
         cout << num << " ";
      }
      cout << "\n";
      return;
   }

   answer.push_back(0);
   backtracking(cur + 1);
   answer.pop_back();

   answer.push_back(1);
   backtracking(cur + 1);
   answer.pop_back();
}

int main() {
   cin >> n;
   backtracking(n);
}