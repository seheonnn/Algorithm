// 백준 15927 회문은 회문아니야!! 완전탐색(시간초과)
//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//bool isPalindrome(string str) {
//   int n = str.size();
//   for (int i = 0; i < n / 2; i++) {
//      if (str[i] != str[n - i - 1])
//         return false;
//   }
//   return true;
//}
//
//int main() {
//   ios_base::sync_with_stdio(false);
//   cin.tie(NULL);
//   cout.tie(NULL);
//   string str;
//   cin >> str;
//
//   int r = -1;
//
//   int n = str.size();
//   for (int i = 0; i < n;i++) {
//      for (int j = i + 1; j < n; j++) {
//         string tmp = str.substr(i, j - i + 1);
//         //cout << tmp << "\n";
//         if (!isPalindrome(tmp)) {
//            r = max(r, (int)tmp.size());
//         }
//      }
//   }
//
//   cout << r << "\n";
//
//   return 0;
//}

// 백준 15927 회문은 회문아니야!! manacher
//#include <iostream>
//#define MAX 500000
//
//using namespace std;
//
//int A[2 * MAX + 1]; // N의 최대값보다 충분하게
//
//bool manacher(const string& str) {
//   string tmp = "#";
//   for (char c : str) {
//      tmp += c;
//      tmp += "#";
//   }
//
//   int n = tmp.size();
//   int r = -1, p = -1;
//
//   for (int i = 0; i < n; i++) {
//      if (i <= r) {
//         int ii = 2 * p - i;
//         A[i] = min(r - i, A[ii]);
//      }
//
//      while (i - A[i] - 1 >= 0 and i + A[i] + 1 < n and tmp[i - A[i] - 1] == tmp[i + A[i] + 1]) {
//         A[i]++;
//      }
//
//      if (i + A[i] > r) {
//         r = i + A[i];
//         p = i;
//      }
//   }
//
//   int original = (n - 1) / 2;
//   return A[n / 2] == original;
//}
//
//// 문자열의 모든 문자가 같은지
//bool checkStringSame(const string& str) {
//   for (char c : str) {
//      if (c != str[0]) {
//         return false;
//      }
//   }
//   return true;
//}
//
//int main () {
//   string str;
//   cin >> str;
//
//   // 팰린드롬이 아니면 전체 문자열의 길이 출력
//   if (!manacher(str)) {
//      cout << str.size() << "\n";
//   }
//   else { // 팰린드롬이면서
//      // 문자열의 문자들이 모두 같다면 -1 출력
//      if (checkStringSame(str)) {
//         cout << -1 << "\n";
//      }
//      // 문자열의 문자들이 모두 같지 않으면 전체 문자열 길이 - 1
//      else {
//         cout << str.size() - 1 << "\n";
//      }
//   }
//
//   return 0;
//}

// 백준 15927 회문은 회문아니야!! 구현
#include <iostream>
#include <algorithm>

using namespace std;

int main() {

   // 문자열 전체가 팰린드롬이 아니면 답은 문자열 전체 길이임
   // 문자열 전체가 팰린드롬임
   // 1) 전체 문자열이 동일한 문자인 경우 답은 -1
   // 2) 아닌 경우 : 전체 길이 - 1
   string str;
   cin >> str;

   bool eq = true;

   int n = str.size();
   for (int i = 0; i < n / 2; i++) {
      if (str[i] != str[n - i - 1]) {
         // 문자열 전체가 팰린드롬이 아니면 답은 문자열 전체 길이임
         cout << n << "\n";
         return 0;
      }
      // 만약 문자열이 팰린드롬이라면
      // 전체 문자가 동일하지 않은 문자열이라면 답은 전체 길이 - 1
      else if (str[i] != str[i + 1]) {
         eq = false;
      }
   }
   // 문자열이 팰린드롬이면서 전체 문자가 동일하다면 답은 -1
   if (eq)
      cout << -1;
   else
      cout << str.length() - 1;

   return 0;
}