#include <string>
#include <vector>
#include <iostream>

using namespace std;

int trans(int sched) {
    int hours = sched / 100;
    int min = sched % 100;

    min += 10;
    if (min >= 60) {
        hours += 1;
        min -= 60;
    }

    return (hours * 100) + min;
}

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = 0;
    int n = schedules.size();
    vector<bool> gift (n, true);
    for (int i = 0; i < n; i++) {

        int limit = trans(schedules[i]);

        for (int j = 0; j < timelogs[0].size(); j++) {
            int today = (j + startday) % 7;
            if (today == 6 || today == 0) continue;

            if (limit < timelogs[i][j]) gift[i] = false;

        }
    }

    for (auto tmp : gift) {
        if (tmp) answer++;
    }

    return answer;
}