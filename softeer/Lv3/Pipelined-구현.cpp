// 소프티어 Lv3 Pipelined
#include <iostream>
#include <algorithm>
#define MAX 200001
using namespace std;

int main() {
   int arr[MAX];
   int n;
   cin >> n;
   for (int i = 0; i < n; i++) {
      cin >> arr[i];
   }

   sort(arr, arr + n);

   int tmp = 0;
   for (int i = 0; i < n; i++) {
      tmp = max(tmp, arr[i]);
   }

   cout << tmp + (n - 1) << "\n";

   return 0;
}