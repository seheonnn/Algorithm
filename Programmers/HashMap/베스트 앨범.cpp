#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    map<string, int> genresCnt; // 장르별 총 재생 횟수 (map은 자동 정렬됨)
    map<string, vector<pair<int, int>>> genresCntVec; // 장르별 [고유번호, 재생횟수] 저장

    for (int i = 0; i < genres.size(); i++) {
        genresCnt[genres[i]] += plays[i];
        genresCntVec[genres[i]].push_back({i, plays[i]});
    }

    // 장르별 노래를 재생 횟수 기준으로 정렬 (내림차순, 재생 횟수가 같으면 고유 번호 오름차순)
    for (auto& g : genresCntVec) {
        sort(g.second.begin(), g.second.end(), [](pair<int, int> a, pair<int, int> b) {
            return a.second == b.second ? a.first < b.first : a.second > b.second;
        });
    }

    // 장르를 총 재생 횟수 기준으로 정렬
    vector<pair<string, int>> sortedGenresCnt(genresCnt.begin(), genresCnt.end());// Map을 파싱하여 정렬
    sort(sortedGenresCnt.begin(), sortedGenresCnt.end(), [](pair<string, int> a, pair<string, int> b) {
        return a.second > b.second;
    });

    vector<int> answer;
    // 각 장르별로 최대 2곡을 선택
    for (auto& genre : sortedGenresCnt) {
        auto& songs = genresCntVec[genre.first];
        answer.push_back(songs[0].first);
        if (songs.size() > 1) {
            answer.push_back(songs[1].first);
        }
    }

    return answer;
}