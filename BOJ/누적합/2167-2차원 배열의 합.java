import java.io.*;
import java.util.*;

public class Main {
    static int n, m, k;
    static int[][] arr;
    static int[][] prefix;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n + 1][m + 1];
        prefix = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                prefix[i][j] = arr[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]; // 누적합 계산. 중복값 제외
            }
        }

        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        for (int q = 0; q < k; q++) {
            st = new StringTokenizer(br.readLine());
            int i, j, x, y;
            i = Integer.parseInt(st.nextToken());
            j = Integer.parseInt(st.nextToken());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());

            // i, j ~ x, y까지의 합, i - 1, y와 x, j - 1 중복 제거 유의 !!
            System.out.println(prefix[x][y] - (prefix[i - 1][y] + prefix[x][j - 1]) + prefix[i - 1][j - 1]);
        }
    }
}