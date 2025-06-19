#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    vector<int> scores = {0, 3, 2, 1, 0, 1, 2, 3};


    map<char, int> hm = {{'R', 0}, {'T', 0}, {'C', 0}, {'F', 0}, {'J', 0}, {'M', 0}, {'A', 0}, {'N', 0}};
    for (int i = 0; i < survey.size(); i++) {
        if (choices[i] < 4) {
            hm[survey[i][0]] += scores[choices[i]];
        } else if (choices[i] > 4) {
            hm[survey[i][1]] += scores[choices[i]];
        } else {
            continue;
        }

        // scores 배열 대신
//        int score = choices[i] - 4;
//        if (score < 0) {
//            hm[survey[i][0]] += -score; // 비동의 쪽에 점수
//        } else if (score > 0) {
//            hm[survey[i][1]] += score;  // 동의 쪽에 점수
//        }
    }

    if (hm['R'] < hm['T']) answer += 'T';
    else answer += 'R';

    if (hm['C'] < hm['F']) answer += 'F';
    else answer += 'C';

    if (hm['J'] < hm['M']) answer += 'M';
    else answer += 'J';

    if (hm['A'] < hm['N']) answer += 'N';
    else answer += 'A';

    // if 문 대신
//    vector<pair<char, char>> indicators = {
//    {'R', 'T'}, {'C', 'F'}, {'J', 'M'}, {'A', 'N'}
//    };
//
//    for (auto [a, b] : indicators) {
//        if (hm[a] < hm[b]) answer += b;
//        else answer += a;
//    }


    return answer;
}