// 프로그래머스 여행경로 DFS
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

vector<string> answer;
map<string, vector<string>> hm;
map<string, map<string, int>> visited;

void DFS(string cur) {
    for (auto next : hm[cur]) {
        if (visited[cur][next] > 0) {
            visited[cur][next]--;
            DFS(next);
        }
    }
    answer.push_back(cur); // 경로 중간에 넣으면 이후 경로가 바뀌었을 떄 를 고려하지 못함. 모든 경로를 다 탐색한 후에 추가.
}

vector<string> solution(vector<vector<string>> tickets) {

    for (auto tmp : tickets) {
        hm[tmp[0]].push_back(tmp[1]);
        visited[tmp[0]][tmp[1]]++;
    }

    for (auto& tmp : hm) {
        // 사전순 정렬. BFS 순서를 보장하지 않으므로 DFS를 사용해야. 백트래킹으로도 풀 수 있음
        sort(tmp.second.begin(), tmp.second.end()); // first : key, second : value
    }

    DFS("ICN");
    reverse(answer.begin(), answer.end());
    return answer;
}