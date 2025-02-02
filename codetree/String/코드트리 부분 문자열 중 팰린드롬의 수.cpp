// // 코드트리 부분 문자열 중 팰린드롬의 수 완전탐색(시간초과)
// #include <iostream>

// using namespace std;

// bool isPalindrome(string str) {
//     int n = str.size();
//     for (int i = 0; i < n / 2;i++) {
//         if (str[i] != str[n - i - 1]) {
//             return false;
//         }
//     }
//     return true;
// }

// int main() {
//     string str;
//     cin >> str;

//     int r = 0;
//     int len = str.size();
//     for (int i = 0; i < len; i++) {
//         for (int j = i + 1; j <= len; j++) {
//             string tmp = str.substr(i, j - i );
//             if (isPalindrome(tmp)) {
//                 r++;
//             }
//         }
//     }
//     cout << r << "\n";
//     return 0;
// }

// 코드트리 부분 문자열 중 팰린드롬의 수 Manacher's Algorithm
#include <iostream>
#include <string>
#include <algorithm>

#define MAX 200001

using namespace std;

// Manacher's Algorithm을 이용하여 문자열 내 팰린드롬 개수를 계산하는 함수
long long manacher(string str) {
    string tmp;

    // 문자열을 전처리하여 문자 사이에 #을 추가
    for (char c : str) {
        tmp += "#";
        tmp += c;
    }
    tmp += "#";

    int n = (int)tmp.size();
    int arr[MAX] = {0};
    int r = -1, p = -1; // r: 최대 팰린드롬 범위, p: 해당 중심 인덱스
    long long ans = 0;

    // Manacher's Algorithm 수행
    for (int i = 0; i < n; i++) {
        if (r >= i) {
            int ii = 2 * p - i;
            arr[i] = min(r - i, arr[ii]);
        }

        // i를 중심으로 확장
        while (i - arr[i] - 1 >= 0 && i + arr[i] + 1 < n && tmp[i - arr[i] - 1] == tmp[i + arr[i] + 1]) {
            arr[i]++;
        }

        // r과 p 갱신
        if (i + arr[i] > r) {
            r = i + arr[i];
            p = i;
        }
    }

    // 팰린드롬 개수 계산
    for (int i = 0; i < n; i++) {
        int max_len = 2 * arr[i] + 1; // 전체 길이
        int l = max_len / 2;       // 팰린드롬의 절반 길이
        ans += (l + 1) / 2;        // 가능한 팰린드롬의 개수 합산
    }

    return ans;
}

int main() {
    string str;
    cin >> str;

    long long result = manacher(str);
    cout << result << endl;

    return 0;
}
