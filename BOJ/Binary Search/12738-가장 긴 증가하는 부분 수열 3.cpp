// 백준 12738 가장 긴 증가하는 부분 수열 3 이분탐색
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> arr, lst;

int binary_search(vector<int>& v, int target) {
    int left = 0, right = v.size();
    while(left < right) {
        int mid = (left + right) / 2;
        if (v[mid] >= target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

int main() {
    cin >> n;
    arr.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];

        int pos = binary_search(lst, arr[i]);
        if (pos == lst.size()) {
            lst.push_back(arr[i]);
        } else {
            lst[pos] = arr[i];
        }
    }

    cout << lst.size() << endl;

    return 0;
}