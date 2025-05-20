#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

bool cmp (const vector<int>& a, const vector<int>& b) {
    return a.size() < b.size();
}

vector<int> solution(string s) {
    vector<int> answer;

    vector<vector<int>> sets;
    vector<int> cur;
    string num = "";

    for (int i = 1; i < s.size() - 1; i++) {
        if (isdigit(s[i])) {
            num += s[i];
        } else if (s[i] == ',') {
            if (!num.empty()) {
                cur.push_back(stoi(num));
                num = "";
            }
        } else if (s[i] == '{') {
            cur.clear();
        } else if (s[i] == '}') {
            if (!num.empty()) {
                cur.push_back(stoi(num));
                num = "";
            }
            sets.push_back(cur);
        }
    }

    sort(sets.begin(), sets.end(), cmp);

    set<int> r;

    for (const auto& tmp : sets) {
        for (int num : tmp) {
            if (r.find(num) == r.end()) {
                r.insert(num);
                answer.push_back(num);
                break;
            }
        }
    }

    return answer;
}