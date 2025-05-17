// 코드트리 아름다운 수
#include <iostream>
#include <vector>

using namespace std;

int n, cnt;
vector<int> answer;

bool isBeautiful(vector<int>& num) {

   int i = 0;
   while (i < num.size()) {
      int digit = num[i];

      for (int j = 0; j < digit; j++) {
         if (num[i + j] != digit) {
            return false;
         }
      }
      i += digit; // 해당 수만큼 건너뛰기
   }
   return true;
}

void backtracking(int start) {
   if (start == n) {
      if (isBeautiful(answer))
         cnt++;
      return;
   }

   for (int i = 1; i <= 4; i++) {
      answer.push_back(i);
      backtracking(start + 1);
      answer.pop_back();
   }
}

int main() {
   ios::sync_with_stdio(false);
   cin.tie(NULL);
   cout.tie(NULL);

   cin >> n;
   backtracking(0);
   cout << cnt;

   return 0;
}