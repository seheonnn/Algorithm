// 백준 1747 소수&팰린드롬 수 에라토스테네스의 체 & 팰린드롬
//#include <iostream>
//#include <string>
//
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
//// 에라토스테네스의 체 범위 주의 !!
bool isPrime(int n) {
   if (n < 2) return false;
   for (int i = 2; i * i <= n + 1;i++) {
      if (n % i == 0)
         return false;
   }
   return true;
}

int main() {

   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   cout.tie(NULL);

   int num;
   cin >> num;
   for (int i = num; ; i++) {
      if (isPrime(i) and isPalindrome(to_string(i))) {
         cout << i;
         break;
      }
   }

   return 0;
}