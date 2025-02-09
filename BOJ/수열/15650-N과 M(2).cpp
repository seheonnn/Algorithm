#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> answer;
vector<int> visited;

void backtracking(int start) {
    if (answer.size() == m) {
        for (int num : answer) {
            cout << num << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = start; i <= n; i++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            answer.push_back(i);
            backtracking(i + 1);
            answer.pop_back();
            visited[i] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    visited.resize(n + 1, 0);

    backtracking(1);

    return 0;
}