#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string str, bomb;
    cin >> str >> bomb;

    vector<char> stack;
    int bombSize = bomb.size();

    for (char c : str) {
        stack.push_back(c);

        if (stack.size() >= bombSize && stack.back() == bomb.back()) {
            bool check = true;

            for (int i = 0; i < bombSize; i++) {
                if (stack[stack.size() - bombSize + i] != bomb[i]) {
                    check = false;
                    break;
                }
            }

            if (check) {
                for (int i = 0; i < bombSize; i++) {
                    stack.pop_back();
                }
            }
        }
    }

    if (stack.empty()) {
        cout << "FRULA\n";
    } else {
        for (char c : stack) {
            cout << c;
        }
        cout << '\n';
    }

    return 0;
}
