// 프로그래머스 할인 행사 슬라이딩 윈도우
#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    int windowSize = 10;

    map<string, int> wantMap;
    for (int i = 0; i < want.size(); i++) {
        wantMap[want[i]] = number[i];
    }

    map<string, int> discountMap;
    for (int i = 0; i < windowSize; i++) {
        discountMap[discount[i]]++;
    }

    // 첫 번째 윈도우가 조건을 만족하는지 확인
    bool isValid = true;
    for (const auto& tmp : wantMap) {
        if (discountMap[tmp.first] < tmp.second) {
            isValid = false;
            break;
        }
    }
    if (isValid) answer++;

    // 슬라이딩 윈도우
    for (int i = 1; i <= discount.size() - windowSize; i++) {

        discountMap[discount[i - 1]]--;
        discountMap[discount[i + windowSize - 1]]++; // 우측으로 한 칸 이동

        isValid = true;
        for (const auto& tmp : wantMap) {
            if (discountMap[tmp.first] < tmp.second) {
                isValid = false;
                break;
            }
        }
        if (isValid) answer++;
    }

    return answer;
}
