#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> arr;

 bool cmp(int a, int b) {
    return to_string(a) + to_string(b) > to_string(b) + to_string(a);
 }

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }

    sort(arr.begin(), arr.end(), cmp);

    for (int i = 0 ; i < n; i++) {
        cout << arr[i];
    }

    return 0;
}
