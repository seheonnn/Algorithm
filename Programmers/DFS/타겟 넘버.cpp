#include <string>
#include <vector>

using namespace std;

int recursion(vector<int> numbers, int target, int idx, int sum) {
    if (idx == numbers.size()) {
        return sum == target ? 1 : 0;
    }
    return recursion(numbers, target, idx + 1, sum + numbers[idx]) + recursion(numbers, target, idx + 1, sum - numbers[idx]);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    return recursion(numbers, target, 0, 0);
}