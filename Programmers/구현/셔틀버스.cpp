#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 시간 → 분
int toMin(string time) {
    int h = stoi(time.substr(0, 2));
    int m = stoi(time.substr(3, 2));
    return h * 60 + m;
}

// 분 → "HH:MM" (to_string + 자릿수 맞추기)
string toString(int time) {
    int h = time / 60;
    int m = time % 60;

    string hh = (h < 10 ? "0" : "") + to_string(h);
    string mm = (m < 10 ? "0" : "") + to_string(m);
    return hh + ":" + mm;
}

string solution(int n, int t, int m, vector<string> timetable) {
    vector<int> crew;

    // 크루 도착 시간 정수로 변환 후 정렬
    for (auto time : timetable)
        crew.push_back(toMin(time));
    sort(crew.begin(), crew.end());

    int now = 540; // 09:00
    int idx = 0;

    for (int i = 0; i < n; ++i) {
        int cnt = 0;

        // 이번 셔틀에 탈 수 있는 사람들 태우기
        while (idx < crew.size() && crew[idx] <= now && cnt < m) {
            ++idx;
            ++cnt;
        }

        // 마지막 셔틀이면 판단
        if (i == n - 1) {
            if (cnt < m) return toString(now);              // 자리가 있으면 그냥 와도 됨
            else return toString(crew[idx - 1] - 1);         // 자리가 없으면 한 명 앞에
        }

        now += t; // 다음 셔틀 시간
    }

    return "";
}
