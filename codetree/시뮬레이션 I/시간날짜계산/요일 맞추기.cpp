// 코드트리 요일 맞추기
#include <iostream>

using namespace std;

int m1, d1, m2, d2;
int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string week[] = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

int main() {
    cin >> m1 >> d1 >> m2 >> d2;

    int tmp1 = 0;
    for (int i = 0; i < m1 - 1; i++) {
        tmp1 += days[i];
    }
    tmp1 += d1;

    int tmp2 = 0;
    for (int i = 0; i < m2 - 1; i++) {
        tmp2 += days[i];
    }
    tmp2 += d2;

    int diff = tmp2 - tmp1;
    while (diff < 0) diff += 7; // 음수일 경우 양수가 될 때까지 더함

    cout << week[diff % 7] << endl;

    return 0;
}