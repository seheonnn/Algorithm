#include <string>
#include <vector>
#include <iostream>

using namespace std;

int toSec(string minutes) {
    int min = stoi(minutes.substr(0, 2));
    int sec = stoi(minutes.substr(3));
    return (min * 60) + sec;
}

string toStr(int seconds) {
    int min = seconds / 60;
    int sec = seconds % 60;

    return (min < 10 ? "0" + to_string(min) : to_string(min)) + ":" + (sec < 10 ? "0" + to_string(sec) : to_string(sec));
}

string solution(string video_len, string pos, string op_start, string op_end, vector<string> commands) {
    string answer = "";

    int len = toSec(video_len);
    int cur = toSec(pos);
    int op_s = toSec(op_start);
    int op_e = toSec(op_end);

    for (auto command : commands) {

        if (op_s <= cur && cur <= op_e) cur = op_e;

        if (command == "next") {

            // + 10
            // cur += 10;
            // if (cur >= len) cur = len;
            cur = min(len, cur + 10);

        } else if (command == "prev") {

            // - 10
            // cur -= 10;
            // if (cur <= 0) cur = 0;
            cur = max(0, cur - 10);
        }

        if (op_s <= cur && cur <= op_e) cur = op_e;
    }

    return toStr(cur);
}