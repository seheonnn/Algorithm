#include <iostream>
#include <vector>

using namespace std;

int n, m, k;
vector<vector<int>> arr;
vector<vector<int>> prefix;
int main() {

    scanf("%d %d", &n, &m);

    arr.resize(n + 1, vector<int>(m + 1, 0));
    prefix.resize(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%d", &arr[i][j]);
            prefix[i][j] = arr[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
        }
    }

    scanf("%d", &k);

    for (int t = 0; t < k; t++) {
        int i, j, x, y;
        scanf("%d %d %d %d", &i, &j, &x, &y);
        int r = prefix[x][y] - (prefix[i - 1][y] + prefix[x][j - 1]) + prefix[i - 1][j - 1];
        printf("%d\n", r);
    }

    return 0;
}
