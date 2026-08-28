//http://codeforces.com/gym/106054/problem/B
//No terminado :(

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n, k, r, x;

    cin>>n;
    cin>>k;

    vector<ll> v(n-k+1); 

    for (ll i=0; i<(n-k+1); i++) {
        cin>>v[i];
    }


    for (ll i=0; i<v.size(); i++) {

       //obtener todas las combinaciones de k numeros que sumados den igual a v[x] 
        
    }


    return 0;
}