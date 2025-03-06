import java.io.*;
import java.util.*;

public class Main {
    static String str;
    static String bomb;
    static ArrayList<Character> stack;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        stack = new ArrayList<>();
        str = st.nextToken();
        st = new StringTokenizer(br.readLine());
        bomb = st.nextToken();
        
        for (int i = 0; i < str.length(); i++) {
            stack.add(str.charAt(i));
            if (stack.size() >= bomb.length()) {
                boolean isMatch = true;
                
                // for (int j = 0; j < bomb.length(); j++) {
                //     if (stack.get(stack.size() - bomb.length() + j) == bomb.charAt(j)) {
                //         for (int k = 0; k < bomb.length(); k++) {
                //             stack.remove(stack.size() - 1); // 문자열이 완전히 일치하지 않아도 삭제됨
                //         }
                //     }
                // }

                
                for (int j = 0; j < bomb.length(); j++) {
                    if (stack.get(stack.size() - bomb.length() + j) != bomb.charAt(j)) {
                        isMatch = false;
                        break;
                    }
                }
                
                if (isMatch) {
                    for (int j = 0; j < bomb.length(); j++) {
                            stack.remove(stack.size() - 1);
                        }
                }
            }
        }
        
        if (stack.isEmpty()) {
            System.out.println("FRULA");
        } else {
            StringBuilder sb = new StringBuilder();
            for (char c : stack) {
                sb.append(c);
            }
            System.out.println(sb.toString());
        }
    }
}