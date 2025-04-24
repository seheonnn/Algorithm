// // [1차] 캐시 큐
// #include <string>
// #include <vector>
// #include <deque>

// using namespace std;

// string transForm(string city) {
//     string str = "";
//     for (int i = 0; i < city.size(); i++) {
//         if (65 <= city[i] && city[i] <= 90 ) {
//             str += (city[i] + 32);
//         } else {
//             str += city[i];
//         }
//     }
//     return str;
// }

// bool isExisted(deque<string> queue, string target) {
//     for (int i = 0; i < queue.size(); i++) {
//         if (queue[i] == target) return true;
//     }
//     return false;
// }

// int solution(int cacheSize, vector<string> cities) {
//     int r = 0;
//     deque<string> queue;
//     for (string city : cities) {
//         city = transForm(city);

//         if (isExisted(queue, city)) {
//             r += 1;
//             for (int i = 0; i < queue.size(); i++) {
//                 if (queue[i] == city) {
//                     queue.erase(queue.begin() + i);
//                     break;
//                 }
//             }
//             queue.push_back(city);
//         } else {
//             r += 5;
//             queue.push_back(city);
//             if (queue.size() > cacheSize) {
//                 queue.pop_front();
//             }
//         }
//     }
//     return r;
// }


// [1차] 캐시 Linked List
#include <string>
#include <vector>
#include <list>
#include <algorithm> // find

using namespace std;

string transForm(string city) {
    string str = "";
    for (int i = 0; i < city.size(); i++) {
        if (65 <= city[i] && city[i] <= 90 ) {
            str += (city[i] + 32);
        } else {
            str += city[i];
        }
    }
    return str;
}

int solution(int cacheSize, vector<string> cities) {
    int r = 0;
    list<string> cache; // Linked List

    for (auto city : cities) {
        city = transForm(city);

        auto it = find(cache.begin(), cache.end(), city); // city를 가리키는 iterator 반환
        // it == cache.end() -> 해당 원소가 없음. (cache.end() : 마지막 원소 다음)
        if (it != cache.end()) {
            r += 1;
            cache.erase(it);

            if (cacheSize > 0) {
                cache.push_back(city);
            }
        } else {
            r += 5;
            if (cache.size() >= cacheSize && cacheSize > 0) {
                cache.pop_front();
            }
            if (cacheSize > 0) {
                cache.push_back(city);
            }
        }
    }

    return r;
}