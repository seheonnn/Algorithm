import java.io.*;
import java.util.*;

public class Main {
    static int n, k;
    static int[] coin;
    static int[] dp; // dp[i] : i원을 만들 수 있는 경우의 수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        coin = new int[n + 1];
        dp = new int[k + 1];
        for (int i = 0; i < n; i++)  {
            st = new StringTokenizer(br.readLine());
            coin[i] = Integer.parseInt(st.nextToken());
        }

        dp[0] = 1; // 동전 0원인 경우 1번
        for (int i = 0; i < n; i++) {
            for(int j = coin[i]; j <= k; j++) {
                dp[j] += dp[j - coin[i]];
            }
        }
        System.out.println(dp[k]);
    }
}