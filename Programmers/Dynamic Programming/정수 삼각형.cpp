// 프로그래머스 정수 삼각형 DP
#include <string>
#include <vector>

using namespace std;

vector<vector<int>> dp;

int solution(vector<vector<int>> triangle) {

    int answer = 0;
    dp.assign(triangle.size(), vector<int>());
    for (int i = 0; i < triangle.size(); i++) {
        dp[i].assign(triangle[i].size(), 0);
    }

    dp[0][0] = triangle[0][0];
    for (int i = 1; i < triangle.size(); i++) {
        for (int j = 0; j < triangle[i].size(); j++) {
            if (j == 0) {
                dp[i][j] = dp[i - 1][j] + triangle[i][j];
            } else if (j == triangle[i].size() - 1) {
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j];
            }
        }
    }
    for (int j = 0; j < triangle[triangle.size() - 1].size(); j++) {
        answer = max(answer, dp[triangle.size() - 1][j]);
    }
    return answer;
}