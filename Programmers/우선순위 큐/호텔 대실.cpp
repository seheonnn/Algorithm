#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int toMin(string time) {
    return (stoi(time.substr(0, 2)) * 60) + (stoi(time.substr(3)));
}

int solution(vector<vector<string>> book_time) {
    sort(book_time.begin(), book_time.end());

    // 현재 사용중인 방
    priority_queue<int, vector<int>, greater<int>> room;
    for (auto time : book_time) {
        int start = toMin(time[0]);
        int end = toMin(time[1]) + 10;

        // 우선순위 큐 (내림차순)
        if (!room.empty() && room.top() <= start) room.pop();

        room.push(end);
    }

    return room.size();
}