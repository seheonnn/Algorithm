import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        // Collections.sort()는 ArrayList에

        int i = 0;
        int j = n - 1;
        int cnt = 0;
        while (i < j) { // 조건 주의 !
            if (arr[i] + arr[j] < m) {
                i++;
            } else if (arr[i] + arr[j] > m) {
                j--;
            } else {
                cnt++;
                i++;
                j--;
            }
        }
        System.out.println(cnt);
    }
}