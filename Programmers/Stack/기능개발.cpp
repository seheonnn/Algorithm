#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;
    for (int i = 0; i < progresses.size(); i++) {
        int remain = 100 - progresses[i];
        int day = (remain + speeds[i] - 1) / speeds[i];
        days.push_back(day);
    }

    int cur = days[0];
    int cnt = 0;

    for (int i = 0; i < days.size(); i++) {
        if (days[i] <= cur) {
            cnt++;
        } else {
            answer.push_back(cnt);
            cnt = 1;
            cur = days[i];
        }
    }

    answer.push_back(cnt);

    return answer;
}