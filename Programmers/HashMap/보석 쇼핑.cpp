#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer;

    unordered_map<string, int> curGemsMap; // 현재 윈도우에 포함된 보석
    unordered_set<string> gemsType(gems.begin(), gems.end()); // 전체 보석의 종류
    int start = 0, end = 0;
    int n = gems.size();

    int minLen = gems.size() + 1; // 최대 길이는 gems + 1
    while (end < n) {
        // 오른쪽으로 한 칸 움직여 현재 Map에 포함
        curGemsMap[gems[end]]++;
        end++;

        // 현재 Map의 크기와 전체 보석 종류의 수가 같음 -> 현재 윈도우에 모든 종류의 보석이 포함된 상태
        while (curGemsMap.size() == gemsType.size()) {
            // minLen보다 윈도우 크기가 작다면 갱신
            if (end - start < minLen) {
                minLen = end - start;
                answer = {start + 1, end};
            }

            // start를 1 증가시켜 현재 Map에서 삭제
            curGemsMap[gems[start]]--;
            if (curGemsMap[gems[start]] == 0) curGemsMap.erase(gems[start]);
            start++;
        }

    }

    return answer;
}