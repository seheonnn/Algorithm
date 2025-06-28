// #include <string>
// #include <vector>
// #include <algorithm>

// using namespace std;

// vector<int> solution(vector<string> operations) {
//     vector<int> queue;

//     for (const auto& op : operations) {
//         if (op[0] == 'I') {
//             queue.push_back(stoi(op.substr(2)));
//             sort(queue.begin(), queue.end());
//         } else if(!queue.empty()) {
//             if (op == "D 1") {
//                 queue.erase(queue.end() - 1);
//             } else {
//                 queue.erase(queue.begin());
//             }
//         }
//     }

//     if (queue.empty()) return {0, 0};
//     return {queue.back(), queue.front()};
// }


#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> operations) {
    multiset<int> ms;

    for (const string& op : operations) {
        if (op[0] == 'I') {
            int num = stoi(op.substr(2));
            ms.insert(num);
        } else if (!ms.empty()) {
            if (op[2] == '1') {
                // erase 최대값
                ms.erase(prev(ms.end())); // prev(ms.end()) == ms.end() - 1 in Multiset
            } else {
                // erase 최소값
                ms.erase(ms.begin());
            }
        }
    }

    if (ms.empty()) return {0, 0};
    return {*prev(ms.end()), *ms.begin()};
}
