#include <string>
#include <vector>
#include <climits>

using namespace std;

int answer = INT_MAX;


void dfs(int idx, int sumA, int sumB, const vector<vector<int>>& info, int n, int m, vector<vector<vector<int>>>& visited) {
    if (sumA >= n || sumB >= m) return;
    if (visited[idx][sumA][sumB]) return;

    if (idx == info.size()) {
        answer = min(answer, sumA);
        return;
    }

    visited[idx][sumA][sumB] = true;
    dfs(idx + 1, sumA + info[idx][0], sumB, info, n, m, visited);
    dfs(idx + 1, sumA, sumB + info[idx][1], info, n, m, visited);
}

int solution(vector<vector<int>> info, int n, int m) {
    vector<vector<vector<int>>> visited(info.size() + 1, vector<vector<int>> (n + 1, vector<int>(m + 1)));
    dfs(0, 0, 0, info, n, m, visited);
    return answer == INT_MAX ? -1 : answer;
}
