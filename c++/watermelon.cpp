//Watermelon (4A): https://codeforces.com/problemset/problem/4/A

#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;   
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int w;
    cin>>w;

    if ((w%2==0) && (w!=2)) {
        cout<<"YES";
    } else {
        cout<<"NO";
    }

    return 0;
}
