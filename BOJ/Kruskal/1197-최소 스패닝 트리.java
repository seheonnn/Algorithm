import java.util.*;
import java.io.*;

class Main {
    static int v, e;
    static int[] parents;
    static ArrayList<int[]> graph = new ArrayList<>();

    public static int find(int a) {
        if (parents[a] != a) {
            parents[a] = find(parents[a]);
        }
        return parents[a];
    }

    public static void union(int a, int b) {
        a = find(a);
        b = find(b);

        if (a > b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }

    public static int kruscal() {
        Collections.sort(graph, (o1, o2) -> Integer.compare(o1[0], o2[0]));
        int r = 0, cnt = 0;
        for (int[] tmp : graph) {
            int c = tmp [0];
            int a = tmp[1];
            int b = tmp[2];

            if (find(a) != find(b)) {
                union(a, b);
                r += c;
                cnt++;
                if (cnt == v - 1) break;
            }
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        parents = new int[v + 1];
        for (int i = 0; i <= v; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < e; i++) {
            int a, b, c;
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            graph.add(new int[]{c, a, b});
        }

        System.out.println(kruscal());
    }
}