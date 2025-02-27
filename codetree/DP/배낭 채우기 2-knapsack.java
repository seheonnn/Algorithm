// 코드트리 배낭 채우기 2 DP knapsack
import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[][] dp;
    static int[] weight;
    static int[] value;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dp = new int[n + 1][m + 1];
        weight = new int[n + 1];
        value = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i][j] = 0;
            }
        }

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            weight[i] = Integer.parseInt(st.nextToken());
            value[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (j >= weight[i]) {
                    // 중복을 허용하지 않는 경우랑 dp[i], dp[i-1]차이
                    // i인 경우 현재 동일한 값을 한 번 더 반영, i - 1인 경우 이전 값만 포함
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - weight[i]] + value[i]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }


        int r = 0;
        for (int j = 0; j <= m; j++) {
            r = Math.max(r, dp[n][j]);
        }

        System.out.println(r);
    }
}