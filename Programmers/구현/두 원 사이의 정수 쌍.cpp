#include <cmath>

using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;

    for (long long x = 1; x <= r2; x++) {
        // 가장 바깥 원에서 가능한 y 최대값
        long long maxY = (long long)floor(sqrt(1LL * r2 * r2 - x * x));

        // 가장 안쪽 원에서 가능한 y 최소값
        long long minY = 0;
        if (x < r1) {
            double inner = sqrt(1LL * r1 * r1 - x * x); // 실수 연산이므로 double 유지
            minY = (long long)ceil(inner);
        }

        if (maxY >= minY) {
            answer += (maxY - minY + 1);
        }
    }

    return answer * 4; // 전체 사분면
}
