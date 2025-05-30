#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> arr(n);
    map<int, int> hm;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        cnt += hm[k - arr[i]];  // 지금 숫자와 합쳐서 k 되는 쌍 개수만큼 더함
        hm[arr[i]]++;           // 현재 숫자를 map에 추가
    }

    cout << cnt << endl;
    return 0;
}
