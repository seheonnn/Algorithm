import java.io.*;
import java.util.*;
public class Main {
    static int n, m;
    static ArrayList<Integer> ans;

    public static void backtracking(int start) {
        if (ans.size() == m) {
            for (int num : ans) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i <= n; i++) {
            ans.add(i);
            backtracking(i); // 주의 !!
            ans.remove(ans.size() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ans = new ArrayList<>();

        backtracking(1);
    }
}