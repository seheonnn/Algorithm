#include <string>
#include <vector>
#include <tuple>
#include <algorithm> // 꼭 필요!

using namespace std;

// 전역 변수들
vector<int> left_child;
vector<int> right_child;
vector<int> preorder_result;
vector<int> postorder_result;
vector<tuple<int, int, int>> nodes; // 전역으로 이동

// 정렬 기준 함수
bool cmp(const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
    if (get<1>(a) == get<1>(b)) return get<0>(a) < get<0>(b);
    return get<1>(a) > get<1>(b);
}

// 트리 삽입
void insert(int parent, int child) {
    if (get<0>(nodes[child]) < get<0>(nodes[parent])) { // child의 x가 parent보다 작음 → 왼쪽 자식
        if (left_child[parent] == -1) left_child[parent] = child;
        else insert(left_child[parent], child);
    } else {
        if (right_child[parent] == -1) right_child[parent] = child;
        else insert(right_child[parent], child);
    }
}

// 전위 순회
void preorder(int node) {
    if (node == -1) return;
    preorder_result.push_back(get<2>(nodes[node]));
    preorder(left_child[node]);
    preorder(right_child[node]);
}

// 후위 순회
void postorder(int node) {
    if (node == -1) return;
    postorder(left_child[node]);
    postorder(right_child[node]);
    postorder_result.push_back(get<2>(nodes[node]));
}

// 메인 함수
vector<vector<int>> solution(vector<vector<int>> nodeinfo) {
    int n = nodeinfo.size();

    left_child.assign(n, -1);
    right_child.assign(n, -1);

    // 노드 정보 (x, y, index) 저장
    for (int i = 0; i < n; i++) {
        nodes.push_back({nodeinfo[i][0], nodeinfo[i][1], i + 1});
    }

    // y 기준 내림차순, x 기준 오름차순 정렬
    sort(nodes.begin(), nodes.end(), cmp);

    // 트리 구성
    for (int i = 1; i < n; i++) {
        insert(0, i); // root = index 0
    }

    // 순회
    preorder(0);
    postorder(0);

    return {preorder_result, postorder_result};
}
