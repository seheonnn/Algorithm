#include <string>
#include <vector>
#include <climits>

using namespace std;

int getDist(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    return dx * dx + dy * dy;
}

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;

    for (auto ball : balls) {
        int targetX = ball[0];
        int targetY = ball[1];
        int r = INT_MAX;

        vector<pair<int, int>> targets;
        // 위쪽 벽 기준
        if (!(startX == targetX && startY < targetY)) {
            targets.push_back({targetX, 2 * n - targetY});
        }

        // 아래쪽 벽 기준
        if (!(startX == targetX && startY > targetY)) {
            targets.push_back({targetX, -targetY});
        }

        // 왼쪽 벽 기준
        if (!(startX > targetX && startY == targetY)) {
            targets.push_back({-targetX, targetY});
        }

        // 오른쪽 벽 기준
        if (!(startX < targetX && startY == targetY)) {
            targets.push_back({2 * m - targetX, targetY});
        }

        for (auto target : targets) {
            int dist = getDist(startX, startY, target.first, target.second);
            r = min(r, dist);
        }
        answer.push_back(r);
    }

    return answer;
}