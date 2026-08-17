//Anton and Letters (443A): https://codeforces.com/problemset/problem/443/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;

    getline(cin, s);
    
    unordered_set<char> sSet;

    for (char c : s) {
        if (c >= 'a' && c <= 'z') {
            sSet.insert(c);
        }
    }
    
    cout << sSet.size();

    return 0;
}

