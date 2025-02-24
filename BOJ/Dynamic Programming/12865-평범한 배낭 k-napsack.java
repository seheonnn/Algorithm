// 12865 평번한 배낭 k-napsack

import java.io.*;
import java.util.*;

public class Main {
    static int n, k;
    static int[][] dp;
    static int[] weight;
    static int[] value;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        dp = new int[n + 1][k + 1];
        weight = new int[n + 1];
        value = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            weight[i] = Integer.parseInt(st.nextToken());
            value[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) { // j = 0 아무것도 넣지않은 상태
               if (j >= weight[i]) {
                   // 중복을 허용하지 않는 경우 dp[i - 1][j - weight[i]] + value[i], i : 중복 허용
                   dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
               } else {
                   dp[i][j] = dp[i - 1][j];
               }
            }
        }

        int r = 0;
        for (int j = 0; j <= k; j++) {
            r = Math.max(r, dp[n][j]);
        }

        System.out.println(r);
    }
}