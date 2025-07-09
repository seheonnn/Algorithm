#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> s) {
    vector<string> answer;

    for (string str : s) {
        vector<char> stack;
        int idx110 = 0;
        for (char c : str) {
            stack.push_back(c);

            int len = stack.size();
            if (len >= 3 && stack[len - 3] == '1' && stack[len - 2] == '1' && stack[len - 1] == '0') {
                stack.pop_back();
                stack.pop_back();
                stack.pop_back();
                idx110++;
            }
        }

        // 남은 문자열에서 삽입 위치 찾기 : 마지막 '0'의 위치
        int pos = -1;
        for (int i = stack.size() - 1; i >= 0 ; i--) {
            if (stack[i] == '0') {
                pos = i;
                break;
            }
        }

        string ins = "";
        for (int i = 0; i < idx110; i++) {
            ins += "110";
        }

        string r = "";
        if (pos == -1) {
            // 0이 없으면 맨 앞에 삽입
            r = ins;
            for (char c : stack) {
                r += c;
            }
        } else {
            // 가장 마지막 0 다음에 삽입 -> 0이 1보다 사전순으로 먼저이므로 모든 0 이후에 110 붙이는 게 사전상 앞순서
            for (int i = 0; i <= pos; i++) {
                r += stack[i];
            }
            r += ins;
            for (int i = pos + 1; i < stack.size();i++) {
                r += stack[i];
            }
        }
        answer.push_back(r);
    }


    return answer;
}