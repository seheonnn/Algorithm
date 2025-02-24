// 백준 15663 N과 M(9) 백트래킹

import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Integer> ans;
    static int[] nums;
    static int[] visited;

    static void backtracking() {
        if (ans.size() == m) {
            for (int num : ans) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        int lastUsed = -1; // 재귀함수이므로 재귀가 실행되는 동안 해당 함수도 유지되기 때문에 변수 할당 해제 X
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0 && nums[i] != lastUsed) {
                visited[i] = 1;
                ans.add(nums[i]);
                lastUsed = nums[i]; // 마지막에 사용된 값 저장
                backtracking();
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
        backtracking();
    }
}