// 코드트리 가장 긴 좌우 대칭인 문자열찾기 2 완전탐색(시간초과)
//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//bool isPalindrome(string str) {
//    // string tmp = str;
//    // reverse(str.begin(), str.end());
//    // return tmp == str;
//    int n = str.size();
//    for (int i = 0; i < n / 2; ++i) {
//        if (str[i] != str[n - i - 1]) {
//            return false;
//        }
//    }
//    return true;
//}
//
//
//int main() {
//    // 입출력 속도 최적화
//    ios_base::sync_with_stdio(false); cin.tie(NULL);
//    int r = 0;
//    string str;
//    cin >> str;
//    for (int i = 0; i < str.size(); i++) {
//        for (int j = i + 1; j < str.size(); j++) {
//            string tmp = str.substr(i, j - i); // substr(시작점, 길)
//            if (isPalindrome(tmp)) {
//                int len = tmp.size();
//                r = max(r, len);
//            }
//        }
//    }
//    cout << r << "\n";
//    return 0;
//}


// 코드트리 가장 긴 좌우 대칭인 문자열찾기 2 Manacher's Algorithm
#include <iostream>
#include <string>
#include <algorithm>

#define MAX 200001

using namespace std;

string tmp, str;
int n;
int arr[MAX];

int main() {
    cin >> tmp;

    // 문자열 전처리
    for (int i = 0; i < (int)tmp.size(); i++) {
        str += "#";
        str += tmp[i];
    }
    str += "#";

    n = (int)str.size();
    int r = -1, p = -1;
    int maxLen = 0; // 최장 팰린드롬 길이

    // 마나커 알고리즘
    for (int i = 0; i < n; i++) {
        if (r < i) {
            arr[i] = 0;
        } else {
            int ii = 2 * p - i; // 대칭점
            arr[i] = min(r - i, arr[ii]);
        }

        // 중심 확장
        while (i - arr[i] - 1 >= 0 && i + arr[i] + 1 < n && str[i - arr[i] - 1] == str[i + arr[i] + 1]) {
            arr[i]++;
        }

        // 오른쪽 경계 갱신
        if (i + arr[i] > r) {
            r = i + arr[i];
            p = i;
        }

        // 최장 팰린드롬 길이 갱신
        maxLen = max(maxLen, arr[i]);
    }

    cout << maxLen << endl; // 최장 팰린드롬 반경 출력
    return 0;
}
