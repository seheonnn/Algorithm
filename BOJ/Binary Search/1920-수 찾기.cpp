#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool binary_search(vector<int>& arr, int target, int start, int end) {
    while(start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == target) {
            return true;
        } else if (arr[mid] > target) {
            end = mid - 1;
        } else if (arr[mid] < target) {
            start = mid + 1;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);


    int n, m;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    cin >> m;
    for (int i = 0; i < m; i++) {
        int tmp;
        cin >> tmp;
        cout << binary_search(arr, tmp, 0, n - 1) << "\n";
    }

    return 0;
}

// 재귀이용
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool binary_search(vector<int>& arr, int target, int start, int end) {
    // 종료 조건
    if (start > end) {
        return false;
    }

    int mid = start + (end - start) / 2;

    if (arr[mid] == target) {
        return true;
    } else if (arr[mid] > target) {
        return binary_search(arr, target, start, mid - 1);
    } else {
        return binary_search(arr, target, mid + 1, end);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);


    int n, m;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    cin >> m;
    for (int i = 0; i < m; i++) {
        int tmp;
        cin >> tmp;
        cout << binary_search(arr, tmp, 0, n - 1) << "\n";
    }

    return 0;
}