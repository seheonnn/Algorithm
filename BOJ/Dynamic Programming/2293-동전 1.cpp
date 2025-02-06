// 백준 2293 동전 1
#include <iostream>
#include <climits>
#define MAX 10001

using namespace std;

int n, k;
int coin[101];
int dp[MAX]; // dp[i] : i원을 만드는 경우의 수

int main() {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", coin + i);
    }

    dp[0] = 1;
    for (int i = 0; i < n; i++) {
        for (int j = coin[i]; j <= k; j++) {
            dp[j] += dp[j - coin[i]]; // 동전 coin[i]을 사용하여 j원을 만들 수 있는 경우싀 수
        }
    }

    printf("%d\n", dp[k]);

    return 0;
}