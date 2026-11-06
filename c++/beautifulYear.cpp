// https://codeforces.com/problemset/problem/271/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a, b, c, d;

    cin>>n;

    n+=1;
    
    d=n%10;
    n=n/10;
    c=n%10;
    n=n/10;
    b=n%10;
    n=n/10;
    a=n%10;
    n=n/10;

    while ((a==b) or (b==c) or (c==d) or (d==a)) {
        
        n+=1;
        cout<<n;
        
        d=n%10;
        n=n/10;
        c=n%10;
        n=n/10;
        b=n%10;
        n=n/10;
        a=n%10;
        n=n/10;
    }

    cout<<n;

    return 0;
}