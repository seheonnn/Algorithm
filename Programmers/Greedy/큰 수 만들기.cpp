// 프로그래머스 큰 수 만들기 그리디
#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string number, int k) {
    string answer = "";

    for (auto num : number) {
        // k가 남은 동안 큰 수는 최대한 앞으로
        while (!answer.empty() && answer.back() < num && k > 0) {
            answer.pop_back();
            k--;
        }
        answer += num;
    }

    while(k--) answer.pop_back();

    return answer;
}