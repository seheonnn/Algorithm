// 백준 10757 큰 수 A + B 구현
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
   ios::sync_with_stdio(false);
   cin.tie(NULL);
   cout.tie(NULL);

   string a, b;
   cin >> a >> b;
   while (a.size() > b.size())
      b = '0' + b;
   while (a.size() < b.size())
      a = '0' + a;

   string r = "";
   int tmp = 0;
   for (int i = a.size() - 1; i >= 0; i--) {
      tmp += (a[i] - '0') + (b[i] - '0');
      r = char((tmp % 10) + '0') + r; // r의 앞에 추가
      tmp = tmp / 10;
   }

   if (tmp > 0) // 마지막 자리
      r = char(tmp + '0') + r;
   // r의 뒤에 추가하여 reverse(r.begin(), r.end()); 해도 됨
   cout << r << endl;

   return 0;
}