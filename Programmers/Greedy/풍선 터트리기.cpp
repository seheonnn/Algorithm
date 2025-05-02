#include <string>
#include <vector>

using namespace std;

int solution(vector<int> a) {
    int answer = 0;
    int n = a.size();
    vector<bool> canSurvive(n, false);

    int leftMin = a[0];
    canSurvive[0] = true;
    for (int i = 1; i < n; i++) {
        if (a[i] < leftMin) {
            leftMin = a[i];
            canSurvive[i] = true;
        }
    }

    int rightMin = a[n - 1];
    canSurvive[n - 1] = true;
    for (int i = n - 2; i > 0; i--) {
        if (a[i] < rightMin) {
            rightMin = a[i];
            canSurvive[i] = true;
        }
    }

    for (int i = 0; i < n; i++) {
        if (canSurvive[i]) answer++;
    }

    return answer;
}