import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static long sum, prefixSum; // long 주의 !!
    static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        // ∑xa * xb = (x1) x2 + (x1 + x2) x3 + (x1 + x2 + x3) x4...
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        sum = 0;
        prefixSum = 0;
        for (int i = 0; i < n - 1; i++) {
             prefixSum += arr[i];
             sum += arr[i + 1] * prefixSum;
        }
        System.out.println(sum);
    }
}