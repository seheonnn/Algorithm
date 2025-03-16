#include <iostream>
#include <vector>
#include <string>

using namespace std;

string str;
vector<char> stack;

int main() {
    cin >> str;
    for (auto s : str) {
        if (s == ')') {
            while(!stack.empty()) {
                if (stack.back() == '(') {
                    stack.pop_back();
                    break;
                }
                cout << stack.back();
                stack.pop_back();
            }
        }

        else if (s == '(') {
            stack.push_back(s);
        }

        else if (s == '*' || s == '/') {
            while (!stack.empty() && (stack.back() == '*' || stack.back() == '/')) {
                cout << stack.back();
                stack.pop_back();
            }
            stack.push_back(s);
        }

        else if (s == '+' || s == '-') {
            while (!stack.empty() && (stack.back() == '+' || stack.back() == '-' || stack.back() == '*' || stack.back() == '/')) {// */ 은 우선순위 높으므로 stack에서 출력, stack에 있는 +-는 먼저 나온 연산자이므로 출력
                cout << stack.back();
                stack.pop_back();
            }
            stack.push_back(s);
        }
        else { // 알파벳인 경우
            cout << s;
        }
    }

    while(!stack.empty()) {
        cout << stack[stack.size() - 1];
        stack.pop_back();
    }

    return 0;
}