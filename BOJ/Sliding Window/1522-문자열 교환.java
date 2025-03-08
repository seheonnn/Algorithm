// 백준 1522 문자열 교환 슬라이딩 윈도우

import java.io.*;
import java.util.*;

public class Main {
    static String str;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        str = st.nextToken();
        int len = str.length();

        int cntA = 0;
        for (int i = 0; i < len; i++) {
            if (str.charAt(i) == 'a') {
                cntA++;
            }
        }

        int r = Integer.MAX_VALUE;

        str += str; // 문자열을 2배하여 원형 문자열인 것처럼


        int cntB = 0; // 구간내 b의 개수
        for (int i = 0; i < cntA; i++) {
            if (str.charAt(i) == 'b') {
                cntB++;
            }
        }

        r = cntB;
        // 우측으로 한 칸씩 이동하여 구간 확인 (슬라이딩 윈도우)
        // 구간의 크기는 전체 문자열에서 a의 개수 (cntA)
        for (int i = 1; i < len; i++) {
            // 우측으로 한 칸 이동하여 제외되는 좌측 문자가 b이면 cntB--
            if (str.charAt(i - 1) == 'b') {
                cntB--;
            }

            // 구간에 새롭게 추가되는 문자가 b라면 cntB++
            if (str.charAt(i + cntA - 1) == 'b') {
                cntB++;
            }

            r = Math.min(r, cntB); // 구간 내 포함된 문자 b의 개수가 교체 개수임
            // 모든 a가 연속되어야 하므로
        }

        System.out.println(r);
    }
}