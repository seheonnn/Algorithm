import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] t;
    static int[] p;
    static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        t = new int[n + 1];
        p = new int[n + 1];
        dp = new int[n + 2]; // dp[i]는 i일까지의 최대이익, n + 2 주의 !!
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            t[i] = Integer.parseInt(st.nextToken());
            p[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 1; i <= n; i++) {
            dp[i] = Math.max(dp[i], dp[i - 1]);

            int nextDay = i + t[i];
            if (nextDay <= n + 1) {// n + 1일째 되는 날 퇴사이므로 퇴사일 이전 조건
                dp[nextDay] = Math.max(dp[nextDay], dp[i] + p[i]);
            }
        }
        System.out.println(Math.max(dp[n], dp[n + 1])); // n + 1일이 퇴사일이므로 퇴사일까지의 이익을 고려
    }
}