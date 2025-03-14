// 백준 1806 부분합

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int n, s;
vector<int> arr;
vector<int> dp;

int main() {
    cin >> n >> s;
    arr.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int start = 0, end = 0, curSum = 0;
    int minLength = INT_MAX;

    while (end < n) {
        curSum += arr[end];
        end++;

        while (curSum >= s) { // 현재까지의 합이 기준값보다 크다면
            minLength = min(minLength, end - start); // 현재 개수 갱신
            curSum -= arr[start]; // 앞의 값 제거 후 비교
            start++;
        }
    }

    cout << (minLength == INT_MAX ? 0 : minLength) << endl;

    return 0;
}