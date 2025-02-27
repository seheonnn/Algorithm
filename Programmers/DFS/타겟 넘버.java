class Solution {
    static int recursion(int[] numbers, int target, int idx, int sum) {
        if (idx == numbers.length) {
            return sum == target ? 1 : 0;
        }

        return recursion(numbers, target, idx + 1, sum + numbers[idx]) + recursion(numbers, target, idx + 1, sum - numbers[idx]);
    }

    public int solution(int[] numbers, int target) {
        return recursion(numbers, target, 0, 0);
    }
}