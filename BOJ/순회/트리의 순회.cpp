// 백준 2263 트리의 순회 재귀
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> inorder, postorder;

void getPreorder(int inStart, int inEnd, int postStart, int postEnd) {
    if (inStart > inEnd || postStart > postEnd) {
        return;
    }

    int root = postorder[postEnd];
    cout << root << " ";

    int rootIdx = inStart;
    while (inorder[rootIdx] != root) rootIdx++;

    int leftTreeSize = rootIdx - inStart;

    // 중위 순회에서의 왼쪽 서브트리 범위, 후위 순회에서의 왼쪽 서브트리 범위
    getPreorder(inStart, rootIdx - 1, postStart, postStart + leftTreeSize - 1);
    // 중위 순회에서의 오른쪽 서브트리 범위, 후위 순회에서의 오른쪽 서브트리 범위
    getPreorder(rootIdx + 1, inEnd, postStart + leftTreeSize, postEnd - 1);

}

int main() {
    cin >> n;
    inorder.assign(n, 0);
    postorder.assign(n, 0);
    for (int i = 0; i < n; i++) cin >> inorder[i];
    for (int i = 0; i < n; i++) cin >> postorder[i];

    getPreorder(0, n - 1, 0, n - 1);

    return 0;
}