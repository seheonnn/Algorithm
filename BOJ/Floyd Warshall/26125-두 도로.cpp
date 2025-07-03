#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int n, m, s, t, q;

void FloydWarshall(vector<vector<long long>>& dist) {
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (dist[i][k] < LLONG_MAX && dist[k][j] < LLONG_MAX) { // overflow 방지
                    if (dist[i][j] > dist[i][k] + dist[k][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

int main() {
    cin >> n >> m >> s >> t;
    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, LLONG_MAX));

    for (int i = 1; i <= n; i++) dist[i][i] = 0; // 자기자신은 0으로 초기화

    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        dist[u][v] = min(dist[u][v], w);
    }

    FloydWarshall(dist);

    cin >> q;
    for (int i = 0; i < q; i++) {
        int a1, b1, a2, b2;
        long long c1, c2;
        cin >> a1 >> b1 >> c1 >> a2 >> b2 >> c2;

        long long answer = dist[s][t];

        // s -> a1 -> b1 -> t
        if (dist[s][a1] < LLONG_MAX && dist[b1][t] < LLONG_MAX)
            answer = min(answer, dist[s][a1] + min(c1, dist[a1][b1]) + dist[b1][t]);

        // s -> a2 -> b2 -> t
        if (dist[s][a2] < LLONG_MAX && dist[b2][t] < LLONG_MAX)
            answer = min(answer, dist[s][a2] + min(c2, dist[a2][b2]) + dist[b2][t]);

        // s -> a1 -> b1 -> a2 -> b2 -> t
        if (dist[s][a1] < LLONG_MAX && dist[b1][a2] < LLONG_MAX && dist[b2][t] < LLONG_MAX)
            answer = min(answer, dist[s][a1] + min(c1, dist[a1][b1]) + dist[b1][a2] + min(c2, dist[a2][b2]) + dist[b2][t]);

        // s -> a2 -> b2 -> a1 -> b1 -> t
        if (dist[s][a2] < LLONG_MAX && dist[b2][a1] < LLONG_MAX && dist[b1][t] < LLONG_MAX)
            answer = min(answer, dist[s][a2] + min(c2, dist[a2][b2]) + dist[b2][a1] + min(c1, dist[a1][b1]) + dist[b1][t]);

        if (answer >= LLONG_MAX) cout << -1 << endl;
        else cout << answer << endl;
    }
    return 0;
}
