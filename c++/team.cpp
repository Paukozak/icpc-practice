//Team (231A): https://codeforces.com/problemset/problem/231/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,a,b,c,sal;

    cin>>n;
    sal=0;

    for (int i=0; i<n; i++) {

        cin>>a>>b>>c;

        if ((a+b+c) >= 2) {
            sal+=1;
        }

    }

    cout<<sal;

    return 0;
}