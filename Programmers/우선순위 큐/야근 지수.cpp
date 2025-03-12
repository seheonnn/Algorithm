// 프로그래머스 야근 지수 우선순위 큐
#include <string>
#include <vector>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    priority_queue<int> queue;
    for (auto num : works) {
        queue.push(num);
    }

    while (n--) {
        int tmp = queue.top();
        queue.pop();
        if (tmp > 0) {
            tmp -= 1;
        }
        queue.push(tmp);
    }

    while (!queue.empty()) {
        int num = queue.top();
        queue.pop();
        answer += (num * num);
    }
    return answer;
}