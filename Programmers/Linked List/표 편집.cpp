// 프로그래머스 표 편집 링크드리스트
#include <string>
#include <vector>

using namespace std;

string solution(int n, int k, vector<string> cmd) {
    vector<pair<int, int>> arr(n, pair<int, int> ());
    vector<int> existed(n, 1);
    vector<int> removed;

    for (int i = 0; i < n; i++) {
        arr[i].first = i - 1; // prev
        arr[i].second = i + 1; // next
    }
    arr[n - 1].second = -1;

    int cur = k;

    for (string c : cmd) {
        char tmp = c[0];
        if (tmp == 'U') {
            int x = stoi(c.substr(2));
            while(x --) cur = arr[cur].first;
        } else if (tmp == 'D') {
            int x = stoi(c.substr(2));
            while(x --) cur = arr[cur].second;
        } else if (tmp == 'C') {
            removed.push_back(cur);
            existed[cur] = 0;

            int prev = arr[cur].first;
            int next = arr[cur].second;

            if (prev != -1) arr[prev].second = next;
            if (next != -1) arr[next].first = prev;

            cur = (next != -1) ? next : prev;

        } else if (tmp == 'Z') {
            int tmp = removed.back();
            removed.pop_back();
            existed[tmp] = 1;

            int prev = arr[tmp].first;
            int next = arr[tmp].second;

            if (prev != -1) arr[prev].second = tmp;
            if (next != -1) arr[next].first = tmp;
        }
    }

    string r = "";
    for (int i = 0; i < n; ++i) {
        r += (existed[i] ? 'O' : 'X');
    }

    return r;
}