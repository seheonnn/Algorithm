#include <string>
#include <vector>
#include <set>
#include <tuple>
#include <algorithm>

using namespace std;

bool isValid(set<tuple<int,int,int>> s) {
    for (auto [x, y, a] : s) {
        if (a == 0) { // 기둥
            // 바닥에 걸친 경우, 바로 아래 기둥이 있는 경우, 왼쪽 아래 보가 있는 경우, 왼쪽에 보가 있는 경우 설치 가능
            // .count -> 존재하면 1 반환
            if (y == 0 || s.count({x, y - 1, 0}) || s.count({x - 1, y, 1}) || s.count({x, y, 1})) continue;
            return false;
        } else { // 보
            // 왼쪽 끝이 기둥 위에 있는 경우, 오른쪽 끝이 기둥 위에 있는 경우, 양쪽에 보랑 연결되어 있는 경우 설치 가능
            if (s.count({x, y - 1, 0}) || s.count({x + 1, y - 1, 0}) || s.count({x - 1, y, 1}) && s.count({x + 1, y, 1})) continue;
            return false;
        }
    }
    return true;
}

vector<vector<int>> solution(int n, vector<vector<int>> build_frame) {
    set<tuple<int, int, int>> s;

    for (auto tmp : build_frame) {
        int x = tmp[0], y = tmp[1], a = tmp[2], b = tmp[3];
        tuple<int, int, int> t = {x, y, a};
        if (b == 1) { // 추가
            s.insert(t);
            if (!isValid(s)) s.erase(t);
        } else {
            s.erase(t);
            if (!isValid(s)) s.insert(t);
        }
    }

    vector<vector<int>> answer;
    for (auto [x, y, a] : s) {
        answer.push_back({x, y, a});
    }

    sort(answer.begin(), answer.end());
    return answer;
}