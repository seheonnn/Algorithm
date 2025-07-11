#include <string>
#include <vector>
#include <map>

using namespace std;

map<string, string> parentsMap;
map<string, int> profitMap;

void DFS(string seller, int profit) {
    if (seller == "-" || profit < 1) return;

    int share = profit / 10;
    int tmp = profit - share;
    profitMap[seller] += tmp;
    DFS(parentsMap[seller], share);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer;

    for (int i = 0; i < enroll.size(); i++) {
        parentsMap[enroll[i]] = referral[i];
    }

    for (int i = 0; i < seller.size(); i++) {
        int total = amount[i] * 100;
        DFS(seller[i], total);
    }

    for (auto name : enroll) {
        answer.push_back(profitMap[name]);
    }


    return answer;
}