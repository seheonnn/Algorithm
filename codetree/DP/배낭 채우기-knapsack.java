// 코드트리 배낭 채우기 DP 중복 허용 X
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] weights = new int[n];
        int[] values = new int[n];

        int[]dp = new int[m + 1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            weights[i] = Integer.parseInt(st.nextToken());
            values[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            for (int j = m; j >= weights[i]; j--) { // 역으로
                dp[j] = Math.max(dp[j], dp[j - weights[i]] + values[i]);
            }
        }
        System.out.println(dp[m]);
    }
}