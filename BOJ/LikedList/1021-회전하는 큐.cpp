// 백준 1021 회전하는 큐 회전 큐
#include <iostream>
#include <deque>

using namespace std;

int n, m, x, cnt;
deque<int> queue;

int main() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        queue.push_back(i);
    }

    while(m--) {
        cin >> x;

        // x가 현재 deque에서 몇 번째 인덱스인지 찾기
        int idx = 0;
        for (int i = 0; i < queue.size(); i++) {
            if (queue[i] == x) {
                idx = i;
                break;
            }
        }
        while(1) {
            if (queue.front() == x) {
                queue.pop_front();
                break;
            } else if (idx < queue.size() - idx) {
                queue.push_back(queue.front());
                queue.pop_front();
                cnt++;
            } else {
                queue.push_front(queue.back());
                queue.pop_back();
                cnt++;
            }
        }
    }

    cout << cnt << endl;

    return 0;
}
