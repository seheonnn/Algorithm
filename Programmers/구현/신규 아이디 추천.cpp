#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string new_id) {
    string answer = "";

    for (int i = 0; i < new_id.size(); i++) {
        new_id[i] = tolower(new_id[i]);
    }

    string tmp = "";
    for (char& c : new_id) {
        if (islower(c) || isdigit(c) || c == '-' || c == '_' || c == '.') {
            tmp += c;
        }
    }

    string tmp2 = "";
    for (char& c : tmp) {
        if (c == '.' && !tmp2.empty() && tmp2.back() == '.') continue;
        tmp2 += c;
    }

    if (!tmp2.empty() && tmp2.front() == '.') tmp2.erase(tmp2.begin());
    if (!tmp2.empty() && tmp2.back() == '.') tmp2.pop_back();

    if (tmp2.empty()) tmp2 = "a";

    if (tmp2.size() >= 16) {
        tmp2 = tmp2.substr(0, 15);
        if (tmp2.back() == '.') tmp2.pop_back();
    }

    while (tmp2.size() < 3) {
        tmp2 += tmp2.back();
    }


    return tmp2;
}