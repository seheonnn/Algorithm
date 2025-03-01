// 코드 트리 bit bitmask

import java.io.*;
import java.util.*;

public class Main {
    static int q;
    static int s = 0; // 집합의 상태
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        q = Integer.parseInt(st.nextToken());
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            if (str.equals("add")) {
                int x = Integer.parseInt(st.nextToken());

                if (((s >> x) & 1) == 0) {
                    s ^= (1 << x);
                }

            } else if (str.equals("delete")) {
                int x = Integer.parseInt(st.nextToken());

                if (((s >> x) & 1) == 1) {
                    s ^= (1 << x);
                }

            } else if (str.equals("print")) {
                int x = Integer.parseInt(st.nextToken());

                System.out.println((s >> x) & 1);

            } else if (str.equals("toggle")) {
                int x = Integer.parseInt(st.nextToken());
                s ^= (1 << x);

            } else if (str.equals("clear")) {
                s = 0;

            }
        }
    }
}