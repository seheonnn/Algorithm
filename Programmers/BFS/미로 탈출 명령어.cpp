// 프로그래머스 미로 탈출 명령어 BFS
#include <string>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

char ch[] = {'d', 'l', 'r', 'u'}; // 사전순
int dx[] = {1, 0, 0, -1}; // d, l, r, u
int dy[] = {0, -1, 1, 0};
vector<vector<int>> graph;
string answer = "impossible";

void BFS(int n, int m, int x, int y, int r, int c, int k) {
    // 사전순 유지
    priority_queue<tuple<string, int, int, int>, vector<tuple<string, int, int, int>>, greater<tuple<string, int, int, int>>> q;
    q.push({"", x, y, 0});

    while(!q.empty()) {
        auto [path, x, y, depth] = q.top();
        q.pop();

        int dist = abs(x - r) + abs(y - c);
        // 현재까지 이동거리 + 남은 거리가 k보다 크면 도착할 수 없음
        // 도착지점보다 k가 크다면 남은 거리는 짝수여야 (헛이동)
        if (depth + dist > k || (k - depth - dist) % 2 != 0) continue;

        if (depth == k && x == r && y == c) {
            answer = path;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 1 || n < nx || ny < 1 || m < ny) continue;
            q.push({path + ch[i], nx, ny, depth + 1});
        }

    }
}

// 0 : 빈 칸, 1 : 시작, 2 : 도착
string solution(int n, int m, int x, int y, int r, int c, int k) {
    graph.assign(n + 1, vector<int>(m + 1));

    BFS(n, m, x, y, r, c, k);

    return answer;
}