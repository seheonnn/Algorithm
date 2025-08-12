#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {

    deque<int> q1, q2;
    long long sum1 = 0, sum2 = 0;

    for (auto num : queue1) {
        q1.push_back(num);
        sum1 += num;
    }

    for (auto num : queue2) {
        q2.push_back(num);
        sum2 += num;
    }

    int n = queue1.size() + queue2.size();

    for (int i = 0; i < 3 * n; i++) {
        if (sum1 == sum2) return i;
        if (sum1 > sum2) {
            int tmp = q1.front();
            q1.pop_front();
            q2.push_back(tmp);
            sum1 -= tmp;
            sum2 += tmp;
        } else {
            int tmp = q2.front();
            q2.pop_front();
            q1.push_back(tmp);
            sum1 += tmp;
            sum2 -= tmp;
        }
    }

    return -1;
}