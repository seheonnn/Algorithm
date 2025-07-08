#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    sort(jobs.begin(), jobs.end());

    int time = 0;
    int total = 0;
    int idx = 0;

    while (idx < jobs.size() || !pq.empty()) {
        while (idx < jobs.size() && jobs[idx][0] <= time) {
            pq.push({jobs[idx][1], jobs[idx][0]});
            idx++;
        }

        if (!pq.empty()) {
            auto tmp = pq.top();
            pq.pop();

            time += tmp.first;
            total += (time - tmp.second);
        } else {
            time = jobs[idx][0];
        }
    }

    return total / jobs.size();
}