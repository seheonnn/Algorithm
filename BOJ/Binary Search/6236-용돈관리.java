import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static int n, m;
    static int[] arr;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        int max = 0; // max 가 최소 k
        int total = 0; // total 값이 최대 k

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
            max = Math.max(max, arr[i]);
            total += arr[i];
        }

        int start = max;
        int end = total;
        int r = total;

        while (start <= end) {
            int mid = (start + end) / 2;
            int cnt = 1;
            int money = mid; // 인출 금액

            for (int i = 0; i < n; i++) {
                if (money < arr[i]) {
                    cnt++;
                    money = mid;
                }
                money -= arr[i];
            }

            if (cnt <= m) {
                r = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        System.out.println(r);
    }
}