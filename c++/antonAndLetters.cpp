//Anton and Letters (443A): https://codeforces.com/problemset/problem/443/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;

    getline(cin, s);
    
    std::unordered_set<char> sSet(s.begin(), s.end());

    if (sSet.size()<3) {
        cout<<0;
    } else if (sSet.size()<4) {
        cout<<1;
    } else {
        cout<<(sSet.size()-4);
    }

    return 0;
}

