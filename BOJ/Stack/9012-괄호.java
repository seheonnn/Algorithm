import java.io.*;
import java.util.*;

public class Main {
    static int tc;
    static ArrayList<Character> stack;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        tc = Integer.parseInt(br.readLine());

        for (int t = 0; t < tc; t++) {
            String str = br.readLine();
            stack = new ArrayList<>();

            boolean isValid = true;

            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == '(') {
                    stack.add('(');
                } else if (!stack.isEmpty() && str.charAt(i) == ')') {
                    stack.remove(stack.size() - 1);
                } else { // stack 비었는데 ) 나온 경우
                    isValid = false;
                    break;
                }
            }

            if (isValid && stack.isEmpty()) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
