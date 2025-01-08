// 백준 1021 - 회전하는 큐
#include <iostream>
#include <deque>
#include <algorithm>

#define MAX 50

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    deque<int> queue;
    for (int i = 1; i <= n; i++)
        queue.push_back(i);

    int arr[MAX];
    for (int i = 0; i < m; i++)
        cin >> arr[i];

    int cnt = 0;
    for (int i = 0; i < m; i++) {
        // 현재 위치를 찾음
        auto it = find(queue.begin(), queue.end(), arr[i]);
        int idx = distance(queue.begin(), it);

        // 좌/우 방향 계산
        int left = idx;
        int right = queue.size() - idx;

        // 적은 회전 방향 선택
        if (left <= right) {
            for (int j = 0; j < left; j++) {
                queue.push_back(queue.front());
                queue.pop_front();
            }
            cnt += left;
        }
        else {
            for (int j = 0; j < right; j++) {
                queue.push_front(queue.back());
                queue.pop_back();
            }
            cnt += right;
        }

        // 현재 값을 제거
        queue.pop_front();
    }

    cout << cnt << endl;
    return 0;
}
