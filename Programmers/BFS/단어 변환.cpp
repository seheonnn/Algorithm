// 프로그래머스 단어 변환 BFS
#include <string>
#include <vector>
#include <queue>

using namespace std;

bool canChange(string str, string target) {
    int cnt = 0;
    for(int i = 0; i < str.size(); i++) {
        if (str[i] != target[i]) {
            cnt++;
        }
    }
    return cnt == 1;
}

vector<bool> visited;

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    visited.assign(words.size(), false);
    queue<pair<string, int>> q;
    q.push({begin, 0});

    while (!q.empty()) {
       auto[cur, cnt] = q.front();
        q.pop();
        if (cur == target) {
            return cnt;
        }

        for (int i = 0; i < words.size(); i++) {
            if (!visited[i] && canChange(cur, words[i])) {
                visited[i] = true;
                q.push({words[i], cnt + 1});
            }
        }
    }
    return answer;
}