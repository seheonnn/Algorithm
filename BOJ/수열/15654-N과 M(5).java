import java.io.*;
import java.util.*;
public class Main {
    static int n, m;
    static int[] num;
    static ArrayList<Integer> ans;
    static int[] visited;
    static void backtracking() {
        if (ans.size() == m) {
            for (int n : ans) {
                System.out.print(n + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                ans.add(num[i]);
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
        visited = new int[n];
        num = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(num);

        backtracking();
    }
}