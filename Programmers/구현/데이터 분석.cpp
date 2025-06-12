#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;
    map<string, int> hm = {{"code",0}, {"date",1}, {"maximum",2}, {"remain",3}};

    for (auto vec : data) {
        if (vec[hm[ext]] < val_ext) {
            answer.push_back(vec);
        }
    }

    int sort_idx = hm[sort_by]; // 외부 변수는 []에 작성해야
    sort(answer.begin(), answer.end(), [sort_idx](const vector<int>& a, const vector<int>& b) {
        return a[sort_idx] < b[sort_idx];
    });

    return answer;
}