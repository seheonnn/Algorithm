#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

double win_prob(int fi, int fj) {
    return (4.0 * fi) / (5.0 * fi + 5.0 * fj);
}

double lose_prob(int fi, int fj) {
    return (4.0 * fj) / (5.0 * fi + 5.0 * fj);
}

double draw_prob(int fi, int fj) {
    return (1.0 * (fi + fj)) / (5.0 * fi + 5.0 * fj);
}


int main()
{
    int f[4];
    for (int i = 0; i < 4; i++) {
        cin >> f[i];
    }

// win[i][j]: i번 루돌프가 j번 루돌프를 이길 확률.
// lose[i][j]: i번 루돌프가 j번 루돌프에게 질 확률.
// draw[i][j]: i번 루돌프와 j번 루돌프가 비길 확률.

    double win[4][4] = {0, };
    double lose[4][4] = {0, };
    double draw[4][4] = {0, };

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (i != j) {
                win[i][j] = win_prob(f[i], f[j]);
                lose[i][j] = lose_prob(f[i], f[j]);
                draw[i][j] = draw_prob(f[i], f[j]);
            }
        }
    }

    double total = 0.0;

    // 모든 경기 결과의 가능한 조합 탐색
    // a1, a2, a3: 1번 루돌프가 참여하는 경기 (1번 vs 2번, 1번 vs 3번, 1번 vs 4번).
    // b1, b2: 2번 루돌프가 참여하는 나머지 경기 (2번 vs 3번, 2번 vs 4번).
    // c1: 3번 루돌프가 참여하는 마지막 경기 (3번 vs 4번).
    for (int a1 = 0; a1 < 3; a1++) {
        for (int a2 = 0; a2 < 3; a2++) {
            for (int a3 = 0; a3 < 3; a3++) {
                for (int b1 = 0; b1 < 3; b1++) {
                    for (int b2 = 0; b2 < 3; b2++) {
                        for (int c1 = 0; c1 < 3; c1++) {

                            int score[4] = {0, };

                            // 1번 루돌프 경기
                            // score[0] : 1번 루돌프의 점수, a1 == 0 이면 1번 루돌프가 이긴 것이므로 점수에 3점 추가, a1 == 2라면 1번 루돌프가 비긴 것이므로 1점 추가
                            score[0] += (a1 == 0 ? 3 : (a1 == 2 ? 1 : 0));
                            score[1] += (a1 == 1 ? 3 : (a1 == 2 ? 1 : 0));

                            score[0] += (a2 == 0 ? 3 : (a2 == 2 ? 1 : 0));
                            score[2] += (a2 == 1 ? 3 : (a2 == 2 ? 1 : 0));

                            score[0] += (a3 == 0 ? 3 : (a3 == 2 ? 1 : 0));
                            score[3] += (a3 == 1 ? 3 : (a3 == 2 ? 1 : 0));

                            // 2번 루돌프 경기
                            score[1] += (b1 == 0 ? 3 : (b1 == 2 ? 1 : 0));
                            score[2] += (b1 == 1 ? 3 : (b1 == 2 ? 1 : 0));

                            score[1] += (b2 == 0 ? 3 : (b2 == 2 ? 1 : 0));
                            score[3] += (b2 == 1 ? 3 : (b2 == 2 ? 1 : 0));

                            // 3번 루돌프 경기
                            score[2] += (c1 == 0 ? 3 : (c1 == 2 ? 1 : 0));
                            score[3] += (c1 == 1 ? 3 : (c1 == 2 ? 1 : 0));

                            vector<pair<int, int>> rank;

                            // 점수와 번호 저장
                            for (int i = 0; i < 4; i++) {
                                rank.emplace_back(score[i], -i);
                            }

                            // sort(v.begin(), v.end()): 오름차순
                            // sort(v.rbegin(), v.rend()): 내림차순
                            sort(rank.rbegin(), rank.rend());

                            // rank[0]과 rank[1]은 1등과 2등 루돌프 정보
                            if (-rank[0].second == 0 || -rank[1].second == 0) {
                                double prob = 1.0;

                                // 모든 경기의 확률을 곱함
                                prob *= (a1 == 0 ? win[0][1] : (a1 == 1 ? lose[0][1] : draw[0][1]));
                                prob *= (a2 == 0 ? win[0][2] : (a2 == 1 ? lose[0][2] : draw[0][2]));
                                prob *= (a3 == 0 ? win[0][3] : (a3 == 1 ? lose[0][3] : draw[0][3]));

                                prob *= (b1 == 0 ? win[1][2] : (b1 == 1 ? lose[1][2] : draw[1][2]));
                                prob *= (b2 == 0 ? win[1][3] : (b2 == 1 ? lose[1][3] : draw[1][3]));

                                prob *= (c1 == 0 ? win[2][3] : (c1 == 1 ? lose[2][3] : draw[2][3]));

                                total += prob;
                            }
                        }
                    }
                }
            }
        }
    }

    cout.precision(3); // fixed와 함께 소숫점 3자리 지정, fixed 없으면 전체 중 3자리만 출력
    cout << fixed << total * 100 << endl;

    return 0;
}