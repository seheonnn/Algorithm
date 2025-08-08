#include <string>
#include <vector>

using namespace std;

int answer = 0;
void backtracking(int k, vector<vector<int>> dungeons, vector<int> visited, int cnt) {
    answer = max(answer, cnt);

    for (int i = 0; i < dungeons.size(); i++) {
        if (k >= dungeons[i][0] && visited[i] == 0) { // 최소 피로도
            visited[i] = 1;
            backtracking(k - dungeons[i][1], dungeons, visited, cnt + 1); // 소모 피로도
            visited[i] = 0;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    vector<int> visited(dungeons.size(), 0);
    backtracking(k, dungeons, visited, 0);
    return answer;
}