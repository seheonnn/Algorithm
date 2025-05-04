// 프로그래머스 괄호 회전하기 stack
#include <string>
#include <vector>
#include <vector>

using namespace std;

bool check(string s) {
    vector<char> stack;
    for (auto c : s) {
        if (c == '(' || c == '{' || c == '[')
            stack.push_back(c);
        else {
            if (stack.empty()) return false;
            int n = stack.size();
            char top = stack[n - 1];
            stack.pop_back();
            if (c == ')' && top != '(' ||
            c == '}' && top != '{' ||
            c == ']' && top != '[') return false;
        }
    }
    if (stack.empty()) return true;
    else return false;
}

int solution(string s) {
    int answer = 0;

    for (int i = 0; i < s.size(); i++) {
        if (check(s)) answer++;
        s = s.substr(1) + s[0]; // string 슬라이싱 참고
    }


    return answer;
}