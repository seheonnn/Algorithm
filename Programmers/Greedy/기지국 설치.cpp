int solution(int n, vector<int> stations, int w) {
    int answer = 0;
    int range = w * 2 + 1;  // 기지국 하나가 커버할 수 있는 범위
    int last = 0;  // 마지막으로 커버된 아파트 번호

    for (int s : stations) {
        int left = s - w;  // 현재 기지국이 커버하는 왼쪽 끝
        int right = s + w; // 현재 기지국이 커버하는 오른쪽 끝

        // 현재 기지국의 왼쪽에 빈 구역이 존재하는 경우
        if (left > last + 1) {
            int gap = left - (last + 1);  // 빈 구역의 크기
            answer += (gap + range - 1) / range;  // 필요한 기지국 개수 계산
        }

        last = right; // 현재 기지국이 커버하는 가장 끝 부분을 저장
    }

    // 마지막 기지국 이후에도 빈 구역이 남아있는 경우
    if (last < n) {
        int gap = n - last;
        answer += (gap + range - 1) / range;
    }

    return answer;
}
