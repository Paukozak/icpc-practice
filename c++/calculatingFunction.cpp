// Calculating Function (486A): https://codeforces.com/problemset/problem/486/A

#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;   
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    ll n, result;

    cin>>n;

    result=n/2;

    if (n%2 != 0) {
        result-=n;
    }

    cout<<result;

    return 0;
}
