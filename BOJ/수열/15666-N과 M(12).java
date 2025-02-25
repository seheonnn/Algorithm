// 백준 15666 N과 M(12) 백트래킹
import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Integer> ans;
    static int[] nums;
    static void backtracking(int start) {
        if (ans.size() == m) {
            for (int num  : ans) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        int lastUsed = -1;
        for (int i = start; i < n; i++) {
            if (lastUsed != nums[i]) {
                ans.add(nums[i]);
                lastUsed = nums[i];
                backtracking(i);
                ans.remove(ans.size() - 1);
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
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);
        backtracking(0);
    }
}