// 프로그래머스 광고 삽입 누적합
#include <string>
#include <vector>

using namespace std;

int stringToSec(string time) {
    int h = stoi(time.substr(0, 2));
    int m = stoi(time.substr(3, 2));
    int s = stoi(time.substr(6, 2));

    return (h * 3600) + (m * 60) + s;
}

string secToString(int sec) {
    int h = sec / 3600;
    sec %= 3600;
    int m = sec / 60;
    int s = sec % 60;

    char buf[8];
    sprintf(buf, "%02d:%02d:%02d", h, m, s);
    return string(buf);
}

string solution(string play_time, string adv_time, vector<string> logs) {
    int play_times = stringToSec(play_time);
    int adv_times = stringToSec(adv_time);
    vector<long long> times(360000, 0); // 100시간

    for (auto log : logs) {
        int start = stringToSec(log.substr(0, 8));
        int end = stringToSec(log.substr(9, 8));
        // 누적합 이므로 start부턴 1명 증가, end부턴 1명 감소
        times[start] += 1;
        times[end] -= 1;
    }

    // 시청자수 계산
    for (int i = 1; i <= play_times; i++) {
        times[i] += times[i - 1];
    }

    // 누적 시청 시간 계산
    for (int i = 1; i <= play_times; i++) {
        times[i] += times[i - 1];
    }

    long long max_time = times[adv_times - 1];
    int start = 0;
    for (int i = adv_times; i < play_times; i++) {
        long long total = times[i] - times[i - adv_times];
        if (total > max_time) {
            max_time = total;
            start = i - adv_times + 1;
        }
    }


    return secToString(start);
}