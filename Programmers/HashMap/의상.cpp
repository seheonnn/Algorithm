#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> hm;
    for (auto tmp : clothes) {
        string type = tmp[1];
        hm[type]++;
    }

    for (auto tmp : hm) {
        answer *= (tmp.second + 1); // 각 유형별로 선택하지 않는 경우의 수 1을 추가
    }
    return answer - 1; // 옷을 아예 입지 않는 경우 제외
}