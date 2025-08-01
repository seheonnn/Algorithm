#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;

    for (int i = 0; i < arr.size(); ++i) {
        // answer가 비어있거나, 마지막에 넣은 숫자와 다르면 추가
        if (answer.empty() || answer.back() != arr[i]) {
            answer.push_back(arr[i]);
        }
    }

    return answer;
}