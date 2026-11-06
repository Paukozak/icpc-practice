#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);   

    ll t;
    ll n;
    cin>>t;
    bool listo=false;

    for (int i=0; i<t; i++) {
        cin>>n;

        while ((listo==false) and (n>1)){
            if ((n % 2)==1) {
                cout<<"YES"<<"\n";
                listo=true;
            }
            n=n/2;
        }

        if (listo==false) {
            cout<<"NO"<<"\n";
        }

        listo=false;

    }

    return 0;
}