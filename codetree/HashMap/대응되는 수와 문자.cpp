#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int n, m;

int main() {
    cin >> n >> m;

    vector<string> v(n + 1);
    map<string, int> hm;

    for (int i = 1; i <= n; i++) {
        cin >> v[i];
        hm[v[i]] = i;
    }

    for (int i = 0; i < m; i++) {
        string query;
        cin >> query;

        if (isdigit(query[0])) {
            cout << v[stoi(query)] << endl;
        } else {
            cout << hm[query] << endl;
        }
    }
    return 0;
}
