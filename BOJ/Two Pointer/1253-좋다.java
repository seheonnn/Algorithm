import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static int n;
    static int[] arr;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;

        Arrays.sort(arr);
        for (int i = 0; i < n; i++) {
            int start = 0, end = n - 1;
            int target = arr[i];
            while (start < end) {
                if (start == i) {
                    start++;
                    continue;
                } else if (end == i) {
                    end--;
                    continue;
                }

                if (arr[start] + arr[end] == target) {
                    cnt++;
                    break;
                } else if (arr[start] + arr[end] < target) {
                    start++;
                } else {
                    end--;
                }
            }
        }
        System.out.println(cnt);
    }
}