// 백준 27527 배너 걸기 슬라이딩 윈도우

#include<iostream>
#include<vector>
#include<cmath>
#include<map>

using namespace std;

int n, m;
vector<int> arr;
map<int, int> hm;

int main() {
   cin >> n >> m;
    arr.assign(n, 0);
   int cnt = ceil((9.0 * m)/10);

   for (int i = 0; i < n; i++) {
      cin >> arr[i];
   }

    // 처음 구간
   for (int i = 0; i < m; i++) {
      int cur = arr[i];
      hm[cur]++;
      if (hm[cur] == cnt) { // 특정 높이가 기준만큼 등장하면 YES
         cout << "YES";
         return 0;
      }
   }

    // 슬라이딩 윈도우
   for (int i = m ; i < n; i++) {
      int left = arr[i - m]; // 윈도우에서 제거되는 왼쪽값
      int right = arr[i]; // 윈도우에 추가되는 오른쪽

        hm[left]--;
        hm[right]++;

      if (hm[right] == cnt) {
         cout << "YES";
         return 0;
      }
   }
   cout << "NO";
   return 0;

}