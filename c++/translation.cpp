//Translation (41A): https://codeforces.com/problemset/problem/41/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, n;

    cin>>t>>n;
 
    std::reverse(n.begin(), n.end());

    if (t==n) {
        cout<<"YES";
    } else {
        cout<<"NO";
    }
    

    return 0;
}