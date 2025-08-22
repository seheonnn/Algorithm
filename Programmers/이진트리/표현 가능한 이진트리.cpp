#include <string>
#include <vector>
#include <cmath>

using namespace std;

// length: 문자열 길이. 해당 문자열을 포화 이진트리로 만들 때 필요한 노드 수
int getTreeSize(int length) {
    int h = ceil(log2(length + 1));
    return (1 << h) - 1;
}

// 유효한 이진트리인지 확인
bool isValid(string s, int start, int end) {
    if (start > end) return true;
    int mid = (start + end) / 2;
    char root = s[mid]; // 포화 이진트리 이므로 mid 값이 루트임
    int leftMid = (start + mid - 1) / 2; // 왼쪽 서브트리의 루트
    int rightMid = (mid + 1 + end) / 2; // 우측 서브트리의 루트

    if (root == '0') { // 부모가 0이면 자식도 0이어야
        if (leftMid >= start && s[leftMid] == '1') return false;
        if (rightMid <= end && s[rightMid] == '1') return false;
    }
    return isValid(s, start, mid - 1) && isValid(s, mid + 1, end);
}

vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    for (long long num : numbers) {
        string bin;
        while(num > 0) {
            bin = char('0' + (num%2)) + bin; // long long이므로 char로 변환
            num /= 2;
        }

        int treeSize = getTreeSize(bin.size()); // 포화 이진트리의 노드 수
        bin = string(treeSize - bin.size(), '0') + bin; // treeSize에 맞춰서 이진수 문자열의 길이를 맞추는 것

        if (isValid(bin, 0, bin.size() - 1)) {
            answer.push_back(1);
        } else {
            answer.push_back(0);
        }
    }
    return answer;
}