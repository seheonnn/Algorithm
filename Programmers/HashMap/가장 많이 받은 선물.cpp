#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int solution(vector<string> friends, vector<string> gifts) {
    unordered_map<string, int> hm;
    int n = friends.size();
    vector<vector<int>> graph (n, vector<int>(n));
    vector<int> give(n), receive(n);
    vector<int> score(n);
    for (int i = 0; i < friends.size(); i++) {
        hm[friends[i]] = i;
    }

    for (auto gift : gifts) {
        int idx = gift.find(' ');
        string a = gift.substr(0, idx);
        string b = gift.substr(idx + 1);

        int from_idx = hm[a];
        int to_idx = hm[b];
        graph[from_idx][to_idx]++;
        give[from_idx]++;
        receive[to_idx]++;
    }

    for (int i = 0; i < n; i++) {
        score[i] = give[i] - receive[i];
    }

    vector<int> result(n);

    for (int i = 0 ; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            if (graph[i][j] > graph[j][i]) {
                result[i]++;
            } else if (graph[i][j] == graph[j][i]) {
                if (score[i] > score[j]) result[i]++;
            }
        }
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
        answer = max(answer, result[i]);
    }
    return answer;
}