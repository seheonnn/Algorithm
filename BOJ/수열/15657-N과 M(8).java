// 백준 15657 N과 M(8) 백트래킹

import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Integer> ans;
    static int[] nums;
    static void backtracking(int start) {
        if (ans.size() == m) {
            for (int num : ans) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i < n; i++) {
            ans.add(nums[i]);
            backtracking(i); // 재귀 주의 !!
            ans.remove(ans.size() - 1);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        nums = new int[n];
        ans = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i <n;i ++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);
        backtracking(0);
    }
}