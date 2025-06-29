//// 프로그래머스 단속 카메라 (회의실과 유사)
//#include <string>
//#include <vector>
//#include <climits>
//#include <algorithm>
//
//using namespace std;
//
//vector<pair<int, int>> cam;
//
//int solution(vector<vector<int>> routes) {
//    int answer = 0;
//     int lastCam = INT_MIN;
//
//    for (auto v : routes) {
//        cam.push_back({v[1], v[0]});
//    }
//    sort(cam.begin(), cam.end());
//    for (auto v : cam) {
//        int s = v.second, e = v.first;
//        if (lastCam < s) {
//            lastCam = e;
//            answer++;
//        }
//    }
//    return answer;
//}

#include <string>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 0;

    vector<pair<int, int>> cam;
    int lastCam = INT_MIN;

    // tmp = {진입, 진출}
    for (auto tmp : routes) {
        cam.push_back({tmp[0], tmp[1]});
    }

    sort(cam.begin(), cam.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.second < b.second; // 진출 시점 기준 정렬
    });

    for (auto tmp : cam) {
        int s = tmp.first;
        int e = tmp.second;

        if (lastCam < s) {
            answer++;
            lastCam = e;
        }
    }

    return answer;
}