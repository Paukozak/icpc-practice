//Gravity Flip (405A): https://codeforces.com/problemset/problem/405/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin>>n;
    
    vector<int> v(n);

    for (int i=0; i<n; i++) {
        cin>>v[i];
    }

    sort(v.begin(), v.end());

    for (int x : v) {
        cout << x << " ";
    }

    return 0;
}