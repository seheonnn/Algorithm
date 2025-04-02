#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int n;
int num1, num2;
vector<int> arr;
int main() {
    cin >> n;
    arr.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int r = INT_MAX;
    int sum = 0;
    int start = 0;
    int end = n - 1;
    while(start < end) {
        sum = arr[start] + arr[end];
        if (abs(sum) < r) {
            r = abs(sum);
            num1 = arr[start];
            num2 = arr[end];
        }
        if (sum < 0) start++;
        else end--;
    }

    cout << num1 << " " << num2;
    return 0;
}