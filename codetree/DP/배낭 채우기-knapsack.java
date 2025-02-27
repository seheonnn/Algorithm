// 코드트리 배낭 채우기 DP
import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] weight;
    static int[] value;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        dp = new int[n + 1] [m + 1]; // dp[i][j] :  i개의 보석을 고려했을 때, 무게 j 이하로 가방을 채울 수 있는 최대 가치
        value = new int[n + 1];
        weight = new int[n + 1];

        for(int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            weight[i] = Integer.parseInt(st.nextToken());
            value[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++){
                dp[i][j] = Integer.MIN_VALUE;
            }
        }
        dp[0][0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (j >= weight[i]) { // i번째 보석이 현재 수용 가능한 무게 j보다 작다면 가방에 포함
                    // 수용한다면 가능한 무게 j에서 i보석의 무게를 빼주고 가치 더하기
                    dp[i][j] = Math.max(dp[i - 1][j - weight[i]] + value[i], dp[i - 1][j]);
                } else {
                    // 그대로 유지
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        int r = 0;
        for (int j = 0; j <= m; j++) {
            r = Math.max(r, dp[n][j]); //  n개의 보석을 고려했을 때, 무게 j 이하에서 얻을 수 있는 최대 가치
        }

        System.out.println(r);
    }
}