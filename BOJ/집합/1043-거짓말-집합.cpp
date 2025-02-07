// 백준 1043 거짓말 집합
#include <iostream>
#include <vector>
#define MAX 51

using namespace std;

int n, m, t;

vector<int> set;
vector<int> trueP;

int find(int a) {
	if (set[a] != a) {
		set[a] = find(set[a]);
	}
	return set[a];
}

void unionCus(int a, int b) {
	a = find(a);
	b = find(b);

	if (a != b) {
		set[b] = a;
	}
	/*if (a < b) {
		set[b] = a;
	}
	else {
		set[a] = b;
	}*/
}

bool check(int a, int b) {
	return find(a) == find(b);
}

int main() {
	cin >> n >> m;
	set.resize(n + 1, 0);
	for (int i = 1; i <= n; i++) {
		set[i] = i;
	}

	cin >> t;
	trueP.resize(t, 0);
	for (int i = 0; i < t; i++) {
		cin >> trueP[i];
	}

	vector<vector<int>> party(m); // m개의 vector로 이루어진 vector

	for (int i = 0; i < m; i++) {
		int tmp;
		cin >> tmp;
		party[i].resize(tmp, 0);
		for (int j = 0; j < tmp; j++) {
			cin >> party[i][j];
		}
	}

	for (int i = 0; i < m; i++) {
		int group = party[i][0];
		int len = party[i].size();
		for (int j = 1; j < len; j++) {
			unionCus(group, party[i][j]);
		}
	}

	int r = 0;
	for (int i = 0; i < m; i++) {
		bool canLie = true;
		int par = party[i][0];
		for (int j = 0; j < t; j++) {
			if (check(par, trueP[j])) {
				canLie = false;
			}
		}
		if (canLie) {
			r++;
		}
	}

	cout << r << endl;

	return 0;
}