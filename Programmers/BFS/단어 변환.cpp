#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<bool> visited;

bool canChange(string cur, string target) {
    int cnt = 0;
    for (int i = 0; i < cur.size(); i++) {
        if (cur[i] != target[i]) cnt++;
    }
    return cnt == 1;
}

int BFS(string begin, string target, vector<string> words) {
    queue<pair<string, int>> q;
    q.push({begin, 0});

    while(!q.empty()) {
        auto [cur, cnt] = q.front();
        q.pop();

        if (cur == target) return cnt;

        for (int i = 0; i < words.size(); i++) {
            if (!visited[i] && canChange(cur, words[i])) {
                q.push({words[i], cnt + 1});
                visited[i] = true;
            }
        }
    }
    return 0;
}

int solution(string begin, string target, vector<string> words) {
    visited.assign(words.size(), false);

    return BFS(begin, target, words);
}