import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static ArrayList<Integer> ans;
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void backtracking() throws IOException {
        if (ans.size() == m) {
            for (int num : ans) {
                bw.write(num + " ");
            }
            bw.write("\n");  // 줄바꿈 추가
            return;
        }

        for (int i = 1; i <= n; i++) {
            ans.add(i);
            backtracking();
            ans.remove(ans.size() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ans = new ArrayList<>();

        backtracking();
        bw.flush();  // 출력 버퍼를 한 번에 비움 (시간 초과 방지)
        bw.close();
    }
}

import java.io.*;
// import java.util.*;
// public class Main {
//     static int n, m;
//     static ArrayList<Integer> ans;

//     public static void backtracking() {
//         if (ans.size() == m) {
//             for (int num : ans) {
//                 System.out.print(num + " ");
//             }
//             System.out.println();
//             return;
//         }

//         for (int i = 1; i <= n; i++) {
//             ans.add(i);
//             backtracking();
//             ans.remove(ans.size() - 1);
//         }
//     }

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         n = Integer.parseInt(st.nextToken());
//         m = Integer.parseInt(st.nextToken());
//         ans = new ArrayList<>();

//         backtracking();
//     }
// }