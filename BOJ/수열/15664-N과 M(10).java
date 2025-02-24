// 백준 15664 N과 M(10) 백트래킹

import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Integer> ans;
    static int[] nums;
    static int[] visited;
    static void backtracking(int start) {
        if (ans.size() == m) {
            for (int num : ans) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        int lastUsed = -1;
        for (int i = start; i < n; i++) {
            if (visited[i] == 0 && lastUsed != nums[i]) {
                visited[i] = 1;
                ans.add(nums[i]);
                lastUsed = nums[i];
                backtracking(i);
                ans.remove(ans.size() - 1);
                visited[i] = 0;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ans = new ArrayList<>();
        nums = new int[n];
        visited = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i <n;i ++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);
        backtracking(0);
    }
}