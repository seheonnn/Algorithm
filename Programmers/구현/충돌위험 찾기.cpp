#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

string trans(int x, int y) {
    return to_string(x) + "," + to_string(y);
}

int solution(vector<vector<int>> points, vector<vector<int>> routes) {
    int answer = 0;
    vector<vector<int>> pos (points.size() + 1, vector<int>());
    for (int i = 0; i < points.size(); i++) {
        pos[i + 1].push_back(points[i][0]);
        pos[i + 1].push_back(points[i][1]);
    }

    // vector<unordered_map<string, int>> timeline (10000); // 에러
    unordered_map<int, unordered_map<string, int>> timeline; // time 사이즈를 알 수 없음

    for (auto route : routes) { // 각 로봇의 출발점
        int curX = pos[route[0]][0];
        int curY = pos[route[0]][1];
        int time = 0;
        timeline[time][trans(curX, curY)]++;

        for (int i = 1; i < route.size(); i++) { // 지나야 하는 위치
            int desX = pos[route[i]][0];
            int desY = pos[route[i]][1];

            while ( curX != desX) {
                if (curX < desX) curX++;
                else curX--;
                time++;
                timeline[time][trans(curX, curY)]++;
            }

            while (curY != desY) {
                if (curY < desY) curY++;
                else curY--;
                time++;
                timeline[time][trans(curX, curY)]++;
            }
        }
    }

    for (const auto& [t, position] : timeline) {
        for (const auto& [pos, cnt] : position) {
            if (cnt >= 2) answer++;
        }
    }

    return answer;
}