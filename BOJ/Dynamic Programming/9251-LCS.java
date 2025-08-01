import java.util.*;
import java.io.*;

class Main {
    static String str1, str2;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str1 = br.readLine();
        str2 = br.readLine();

        int n = str1.length();
        int m = str2.length();
        dp = new int[n + 1][m + 1]; // str1의 첫 글자 i와 str2의 첫 글자 j를 비교했을 때 만들 수 있는 최장 공통 부분 수열의 길이
        for (int i = 1; i <= n;i++) {
            for (int j = 1; j <= m; j++) {
                if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        System.out.println(dp[n][m]);
    }
}