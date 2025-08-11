#include <string>
#include <vector>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups) {
    long long answer = 0;
    long long d = 0;
    long long p = 0;

    for (int i = n - 1; i >= 0; i--) {
        d += deliveries[i];
        p += pickups[i];

        while (d > 0 || p > 0) {
            d -= cap;
            p -= cap;

            answer += ((i + 1) * 2LL); // cap 만큼 수거 or 배달하는데 남아 있으면 물류창고까지 왕복
        }
    }
    return answer;
}