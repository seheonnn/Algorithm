// 백준 1158 - 요세푸스 문제
#include <iostream>
#include <deque>

using namespace std;
int main() {
   int n, k;
   cin >> n >> k;

   deque<int> queue;
   for (int i = 1; i <= n; i++) {
      queue.push_back(i);
   }
   k -= 1;
   cout << "<";
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < k; j++) {
         queue.push_back(queue.front());
         queue.pop_front();
      }

      if (i == n - 1) {
         cout << queue.front();
         queue.pop_front();
      }
      else {
         cout << queue.front() << ", ";
         queue.pop_front();

      }
   }
   cout << ">";
   return 0;
}