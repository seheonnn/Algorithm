// 프로그래머스 이중우선순위큐
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> queue;

    for (const auto& op : operations) {
        if (op[0] == 'I') {
            queue.push_back(stoi(op.substr(2)));
            sort(queue.begin(), queue.end());
        }
        else if (!queue.empty()) {
            if (op == "D 1") {
                queue.erase(queue.end() - 1);
            }
            else if (op == "D -1") {
                queue.erase(queue.begin());
            }
        }
    }

    if (queue.empty()) return {0, 0};
    return {queue.back(), queue.front()};
}
