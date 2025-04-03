#include <algorithm>
#include <string>

using namespace std;

int getPalinedrome(string s, int left, int right) {
    while(left >= 0 && right < s.size() && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

int solution(string s)
{
    int answer=0;
    for (int i = 0; i < s.size(); i++) {
        int len1 = getPalinedrome(s, i, i); // i가 중심인 경우
        int len2 = getPalinedrome(s, i, i + 1); // i와 i + 1이 중심인 경우
        answer = max({answer, len1, len2});
    }

    return answer;
}