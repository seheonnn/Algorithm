import java.io.*;
import java.util.*;

public class Main {
    static int n, cnt;
    static int[] board; // board[i] : i행에 퀸이 배치된 열

    // 현재 퀸을 row에 놓을 때 비교
    public static boolean isPoss(int row) {
        for (int i = 0; i < row; i++) {
            // 이전에 놓은 i와 같은 열이면 안 됨 or i와 같은 대각선상에 있으면 안 됨 (직접 그려보기)
            if (board[row] == board[i] || row - i == Math.abs(board[row] - board[i])) {
                return false;
            }
        }
        return true;
    }

    public static void backtracking(int row) {
        if (row == n) {
            cnt++;
            return;
        }

        // 각 행(row)에 대해 가능한 모든 열(column)을 탐색
        for (int i = 0; i < n; i++) {
            board[row] = i;
            if (isPoss(row)) {
                // 동일한 row를 호출하지 않기 때문에 row != i인지 확인할 필요 X
                backtracking(row + 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        board = new int[n];
        backtracking(0);

        System.out.println(cnt);
    }
}