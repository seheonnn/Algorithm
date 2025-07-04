// 프로그래머스 입국심사 이분탐색
#include <string>
#include <vector>
#include <climits>
#include <iostream>
using namespace std;

long long solution(int n, vector<int> times) {

    long long answer = 0;
    long long left = LONG_MAX, right = 0;
    for (auto time : times) {
        left = min(left, (long long) time);
        right = max(right, (long long) time);
    }

    right *= n; // 최악의 경우. 가장 느린 심사관이 모두 처리

    while (left <= right) {
        long long mid = (left + right) / 2;
        long long people = 0;

        for (auto time : times) {
            people += (mid / time);
            if (people >= n) break;
        }

        if (people >= n) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }


    }

    return answer;
}