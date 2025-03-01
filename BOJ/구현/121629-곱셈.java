// 121629 곱셈 구현

import java.io.*;
import java.util.*;

public class Main {
    static int a, b, c;
    static int r = 1;

    public static long func(int a, int b, int c) {
        if (b == 1) {
            return a % c;
        }

        long half = func(a, b / 2, c);  // A^(B/2) % C 재귀적으로 계산
        half = (half * half) % c;       // 중간 결과를 제곱하여 모듈러 연산 적용

        if (b % 2 == 1) { // B가 홀수일 경우, 한 번 더 A를 곱해줌 ex) A^11 = A^5 * A^5 * A
            half = (half * a) % c;
        }

        return half;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        System.out.println(func(a, b, c));
    }
}