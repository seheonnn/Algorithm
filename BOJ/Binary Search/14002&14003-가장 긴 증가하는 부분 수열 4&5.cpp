// 백준 14002 & 14003 가장 긴 증가하는 부분 수열 4&5 이분탐색
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> arr, lst, parents;

int binary_search(vector<int>& v, int target) {
    int left = 0, right = v.size();
    while (left < right) {
        int mid = (left + right) / 2;
        if (v[mid] >= target) right = mid;
        else left = mid + 1;
    }
    return left;
}

int main() {
    cin >> n;
    arr.resize(n);
    parents.assign(n, -1);

    vector<int> idx; // LIS 원소의 실제 인덱스를 저장

    for (int i = 0; i < n; i++) {
        cin >> arr[i];

        int pos = binary_search(lst, arr[i]);

        if (pos == lst.size()) {
            lst.push_back(arr[i]);
            idx.push_back(i); // lst 배열의 인덱스 저장
        } else {
            lst[pos] = arr[i];
            idx[pos] = i;
        }

        if (pos > 0) parents[i] = idx[pos - 1]; // 이전 idx 원소 저장
    }

    cout << lst.size() << endl;

    vector<int> r;
    int lastIdx = idx.back(); // idx 배열의 마지막 원소

    while (lastIdx != -1) {
        r.push_back(arr[lastIdx]);
        lastIdx = parents[lastIdx];
    }

    // 역순 출력
    for (int i = r.size() - 1; i >= 0; i--) {
        cout << r[i] << " ";
    }

    return 0;
}
