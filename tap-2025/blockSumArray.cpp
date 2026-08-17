//http://codeforces.com/gym/106054/problem/B
//No terminado :(

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, cantAr, r, x;

    cin>>n;
    cin>>k;

    vector<int> v(n-k+1); 

    for (int i=0; i<(n-k+1); i++) {
        cin>>v[i];
    }

    cantAr=(n+k-1)/k; //division redondeada para arriba 

    for (int i=0; i<cantAr; i++) {

       //obtener todas las combinaciones de k numeros que sumados den igual a v[x] 
        
    }


    return 0;
}