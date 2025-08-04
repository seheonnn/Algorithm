#include <iostream>
#include <vector>

using namespace std;

int main() {
    string str1, str2;
    cin >> str1;
    cin >> str2;
    int n = str1.size();
    int m = str2.size();

    vector<vector<int>> dp(n + 1, vector<int>(m + 1));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if(str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

     // 2. LCS 문자열 복원
    string lcs = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {
        if (str1[i-1] == str2[j-1]) {
            lcs = str1[i-1] + lcs; // 문자를 추가
            i--;
            j--;
        } else {
            if (dp[i-1][j] > dp[i][j-1])
                i--;
            else
                j--;
        }
    }

    cout << dp[n][m] << endl;
    if (!lcs.empty())
        cout << lcs << endl;

    return 0;
}