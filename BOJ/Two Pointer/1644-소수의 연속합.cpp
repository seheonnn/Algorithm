#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n;
    cin >> n;

    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) primes.push_back(i);
    }


    int start = 0, sum = 0, cnt = 0;
    for (int end = 0; end < primes.size(); end++) {
        sum += primes[end];
        while (sum > n) {
            sum -= primes[start];
            start++;
        }
        if (sum == n) cnt++;
    }

    cout << cnt << "\n";

    return 0;
}