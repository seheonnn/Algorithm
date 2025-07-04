#include <string>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    unordered_set<string> phone_set;

    for (auto phone : phone_book) {
        phone_set.insert(phone);
    }

    for (auto phone : phone_book) {
        for (int i = 0; i < phone.length(); i++) {
            string prefix = phone.substr(0, i);
            if (phone_set.count(prefix)) {
                return false;
            }
        }
    }
    return true;
}