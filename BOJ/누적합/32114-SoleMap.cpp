// 백준 32114 누적합
#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> w;
vector<long long> prefix;  // 차량 수가 최대 10^9까지 가능하므로 long long으로 변경
vector<long long> cars;

int main() {
    scanf("%d %d", &n, &m);
    w.assign(n - 1, 0);
    prefix.assign(n, 0);
    cars.assign(n - 1, 0);

    for (int i = 0; i < n - 1; i++) {
        scanf("%d", &w[i]);
    }

    for (int i = 0; i < m; i++) {
        int u, v, x;
        scanf("%d %d %d", &u, &v, &x);
        prefix[u - 1] += x;
        prefix[v - 1] -= x;
    }

    long long movingCars = 0;

    for (int i = 0; i < n - 1; i++) {
        movingCars += prefix[i];
        cars[i] = movingCars;
    }

    for (int i = 0; i < n - 1; i++) {
        long long c = cars[i];
        long long wi = w[i];

        if (c == 0) {
            printf("0\n");
            continue;
        }

        long long q = c / wi;
        long long r = c % wi;

        long long ans = r * (q + 1) * (q + 1) + (wi - r) * q * q;

        printf("%lld\n", ans);
    }

    return 0;
}
