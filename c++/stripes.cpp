//Stipes (1742C): https://codeforces.com/problemset/problem/1742/C

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, gan;
    string s;

    cin>>n;
    vector<char> v(n);
    
    for (int i=0; i<n; i++) {

        gan=1;

        for (int j=0; j<8; j++) {

            cin>>s;

            set<char> sSet(s.begin(), s.end()); 

            if ((sSet.size()==1) && (s[0]=='R')) {
                gan=0;
            }

        }

        if (gan==0) {
            v[i]='R';
        } else {
            v[i]='B';
        }

    }

    for (char x : v) {
        cout << x << "\n";
    }



    return 0;
}