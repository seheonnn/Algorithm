// 백준 1043 거짓말 집합
import java.io.*;
import java.util.*;
public class Main {

   static int n, m, k;
   static int[] set;
   static int[] trueP;
   static ArrayList<Integer>[] party;

   static int find(int a) {
      if (set[a] != a) {
         set[a] = find(set[a]);
      }
      return set[a];
   }

   static void union(int a, int b) {
      a = find(a);
      b = find(b);

      if (a < b) {
         set[b] = a;
      } else {
         set[a] = b;
      }
   }

   static boolean check(int a, int b) {
      return find(a) == find(b);
   }

   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());

      n = Integer.parseInt(st.nextToken());
      m = Integer.parseInt(st.nextToken());

      // StringTokenizer 는 입력 행이 바뀔 때마다
      st = new StringTokenizer(br.readLine());
      k = Integer.parseInt(st.nextToken());

      set = new int[n + 1];
      party = new ArrayList[m + 1];
      trueP = new int[k];

      for (int i = 0; i < k; i ++) {
         trueP[i] = Integer.parseInt(st.nextToken());
      }

      for (int i = 0; i < m; i ++) {
         st = new StringTokenizer(br.readLine());
         int tmp = Integer.parseInt(st.nextToken());
         party[i] = new ArrayList<>();
         for (int j = 0; j < tmp; j++) {
            party[i].add(Integer.parseInt(st.nextToken()));
         }
      }

      for (int i = 1; i <= n; i++) {
         set[i] = i;
      }

      // 같은 파티 그룹화
      for (int i = 0; i < m; i++) {
         int group = party[i].get(0);
         int len = party[i].size();
         for (int j = 0; j < len; j++) {
            union(group, party[i].get(j));
         }
      }

      int r = 0;
      for (int i = 0; i < m; i++) {
         boolean canLie = true;
         int par = party[i].get(0);
         for (int j = 0; j < k; j++) {
            // 파티에 진실을 아는 사람이 있다면 거짓말 하지 못함
            if (check(par, trueP[j])) {
               canLie = false;
               break;
            }
         }
         if (canLie) {
            r++;
         }
      }
      System.out.println(r);
   }
}
