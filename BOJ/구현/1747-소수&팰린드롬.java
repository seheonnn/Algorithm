// 백준 1747 소수&팰린드롬 수 에라토스테네스의 체 & 팰린드롬
import java.io.*;
import java.util.*;

public class Main {
	static int N;

	public static boolean isPalindrome(String str) {
		int n = str.length();
		for (int i = 0; i < n / 2; i++) {
			if (str.charAt(i) != str.charAt(n - i - 1))
				return false;
		}
		return true;
	}

	public static boolean isPrime(int n) {
		if (n < 2)  return false;
		for (int i = 2; i * i <= n; i++) {
			if (n % i == 0)
				return false;
		}
		return true;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());

		for (int i = N; ; i++) {
			if (isPrime(i) && isPalindrome(String.valueOf(i))) {
				System.out.println(i);
				return;
			}
		}
	}
}
