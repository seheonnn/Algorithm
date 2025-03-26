#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int n, m;
vector<int> visited;
vector<int> ans;
vector<int> arr;
void backtracking(int idx) {

    if (ans.size() == m) {
        for (auto num : ans) {
            cout << num << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            ans.push_back(arr[i]);
            backtracking(idx + 1);
            ans.pop_back();
            visited[i] = 0;
        }
    }

}

int main() {
    cin >> n >> m;
    arr.assign(n, 0);
    visited.assign(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    backtracking(0);
    return 0;
}