#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    int count = 0;
    int num = 666;

    while (true) {
        // 정수를 문자열로 변환해서 "666"이 포함되어 있는지 확인
        if (to_string(num).find("666") != string::npos) {
            count++;
            if (count == n) {
                cout << num << endl;
                break;
            }
        }
        num++;
    }

    return 0;
}
