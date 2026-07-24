//Word on the Paper (1850C): https://codeforces.com/problemset/problem/1850/C

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    char c;

    cin>>n;

    string pal;

    vector<string> v(n);

    for (int x=0; x<n; x++) {
        pal="";
        for (int i=0; i<8; i++) {
            for (int j=0; j<8; j++) {
                cin>>c;

                if (c!='.') {
                    pal=pal+c;
                }
            }
        }

        v[x]=pal;
    }

    for (string x : v) {
        cout << x << "\n";
    }


    return 0;
}