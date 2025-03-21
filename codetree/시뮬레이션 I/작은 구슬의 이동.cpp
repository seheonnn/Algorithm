#include <iostream>

using namespace std;

int n, t;
char d;
int x, y, nd;
int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};
int main() {
    cin >> n >> t;
    cin >> x >> y >> d;

    switch (d) {
        case 'U':
            nd = 1;
            break;
        case 'D':
            nd = 3;
            break;
        case 'L':
            nd = 0;
            break;
        case 'R':
            nd = 2;
            break;
    }

    for (int i = 1; i <= t; i++) {
        int nx = x + dx[nd];
        int ny = y + dy[nd];

        if (nx < 1 || n < nx || ny < 1 || n < ny) {
            nd = (nd + 2) % 4; // 움직이지 않고 방향만 바꿈
        } else {
            x = nx;
            y = ny;
        }
    }

    cout << x << " " << y << endl;

    return 0;
}