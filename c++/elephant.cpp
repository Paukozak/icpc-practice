//Elephant (617A): https://codeforces.com/problemset/problem/617/A

#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;   
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    ll x;

    int result;
    cin>>x;

    if (x<=5) {
        result=1;
    } else {
        result=x/5;
        if ((x%5)!=0) {
            result+=1;
        }
    }

    cout<<result;

    return 0;
}
