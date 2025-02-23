// 백준 15656 N과 M(7) 백트래킹

import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Integer> ans = new ArrayList<>();
    static int[] nums;
    static StringBuilder sb = new StringBuilder();
    // static void bubbleSort(int[] nums) {
    //     for (int i = 0; i < n; i++) {
    //         for (int j = 0; j < n - i - 1; j++) {
    //             if (nums[j] > nums[j + 1]) {
    //                 int tmp = nums[j + 1];
    //                 nums[j + 1] = nums[j];
    //                 nums[j] = tmp;
    //             }
    //         }
    //     }
    // }

    static void backtracking() {
        if (ans.size() == m) {
            for (int num : ans) {
                // System.out.print(num + " ");
                sb.append(num + " ");
            }
            // System.out.println();
            sb.append("\n");
            return;
        }

        for (int i = 0; i < n; i++) {
            ans.add(nums[i]);
            backtracking();
            ans.remove(ans.size() - 1);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ans = new ArrayList<>();
        nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);
        backtracking();

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}